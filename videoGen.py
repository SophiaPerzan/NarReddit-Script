import ffmpeg
import os
import random


class VideoGenerator:
    def __init__(self, env):
        self.env = env

    def generateVideo(self, backgroundVideoFileName, ttsAudioPath, outputVideoPath, directory, subtitlesPath):
        backgroundVideoPath = self.getBackgroundVideoPath(
            backgroundVideoFileName, directory)

        if not os.path.isfile(backgroundVideoPath):
            print(f"Video file not found: {backgroundVideoPath}")
            return False

        if not os.path.isfile(ttsAudioPath):
            print(f"Audio file not found: {ttsAudioPath}")
            return False

        audioDuration = self.getAudioDuration(ttsAudioPath)
        videoProbe = ffmpeg.probe(backgroundVideoPath)
        videoStream = self.getVideoStream(videoProbe)
        videoDuration = float(videoStream['duration'])

        startTime = self.getStartTime(audioDuration, videoDuration)

        # Calculate new dimensions only when necessary
        newWidth, newHeight = None, None
        if videoStream['width'] != 9 or videoStream['height'] != 16:
            newWidth, newHeight = self.getNewDimensions(videoStream)

        video = self.processVideo(
            backgroundVideoPath, videoDuration, audioDuration, startTime, newWidth, newHeight, subtitlesPath)
        audio = ffmpeg.input(ttsAudioPath)

        self.mergeAudioVideo(video, audio, outputVideoPath)

        return outputVideoPath

    def getBackgroundVideoPath(self, backgroundVideoFileName, directory):
        if backgroundVideoFileName.upper() == 'RANDOM':
            return self.getRandomMP4(directory)
        else:
            return os.path.join(directory, self.env['BG_VIDEO_FILENAME'])

    def getAudioDuration(self, ttsAudioPath):
        probe = ffmpeg.probe(ttsAudioPath)
        return float(probe['streams'][0]['duration'])+2

    def getVideoStream(self, videoProbe):
        return next((stream for stream in videoProbe['streams'] if stream['codec_type'] == 'video'), None)

    def getStartTime(self, audioDuration, videoDuration):
        randomizeStart = self.env['RANDOM_START_TIME'].upper() == 'TRUE'
        if videoDuration > audioDuration and randomizeStart:
            return random.uniform(0, videoDuration - audioDuration)
        else:
            return 0

    def getNewDimensions(self, videoStream):
        width = int(videoStream['width'])
        height = int(videoStream['height'])

        if width / height > 9 / 16:  # wider than 9:16, crop sides
            return int(height * (9 / 16)), height
        else:  # narrower than 9:16, crop top and bottom
            return width, int(width * (16 / 9))

    def processVideo(self, backgroundVideoPath, videoDuration, audioDuration, startTime, newWidth, newHeight, subtitlesPath):
        video = ffmpeg.input(backgroundVideoPath)

        # Loop the video if it is shorter than the audio
        if videoDuration < audioDuration:
            loopsNeeded = int(audioDuration // videoDuration) + 1
            videos = [video for _ in range(loopsNeeded)]
            video = ffmpeg.concat(*videos, v=1, a=0)

        # Trim the video to match the length of the audio and crop to the desired aspect ratio
        video = video.trim(start=startTime, end=startTime + audioDuration)
        video = video.setpts('PTS-STARTPTS')

        # Crop the video to the desired aspect ratio if dimensions were calculated
        if newWidth is not None and newHeight is not None:
            video = ffmpeg.filter_(video, 'crop', newWidth, newHeight)

        # Add subtitles if provided
        if subtitlesPath is not None and os.path.isfile(subtitlesPath):
            # Set style for the subtitles
            style = "FontName=Arial,FontSize=20,PrimaryColour=&H00ffffff,OutlineColour=&H00000000," \
                    "BackColour=&H80000000,Bold=0,Italic=0,Alignment=10"
            video = ffmpeg.filter_(
                video, 'subtitles', subtitlesPath, force_style=style)

        return video

    def mergeAudioVideo(self, video, audio, outputVideoPath):
        vcodec = self.env['VCODEC']
        numThreads = self.env['THREADS']
        output = ffmpeg.output(video, audio, outputVideoPath,
                               vcodec=vcodec, threads=numThreads)
        output = ffmpeg.overwrite_output(output)
        ffmpeg.run(output)

    def getRandomMP4(self, directory):
        # Filter the list to include only .mp4 files
        mp4Files = [entry.path for entry in os.scandir(
            directory) if entry.is_file() and entry.name.endswith('.mp4')]

        # Select a random .mp4 file
        randomMP4 = random.choice(mp4Files)

        return randomMP4
