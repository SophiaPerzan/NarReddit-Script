import ffmpeg
import os
import random


class VideoGenerator:
    def __init__(self, env):
        self.env = env

    def generateVideo(self, backgroundVideoPath, ttsAudioPath, outputVideoPath):

        if not os.path.isfile(backgroundVideoPath):
            print(f"Video file not found: {backgroundVideoPath}")
            return False
        if not os.path.isfile(ttsAudioPath):
            print(f"Audio file not found: {ttsAudioPath}")
            return False

        # Get the duration of the audio file
        probe = ffmpeg.probe(ttsAudioPath)
        audio_duration = float(probe['streams'][0]['duration'])+2

        # Get the video's dimensions
        probe = ffmpeg.probe(backgroundVideoPath)
        video_stream = next(
            (stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
        width = int(video_stream['width'])
        height = int(video_stream['height'])
        video_duration = float(video_stream['duration'])

        # Make sure the video is long enough
        if video_duration < audio_duration:
            print(f"The video is not long enough for the audio narration")
            return False

        # Choose a random start time
        start_time = random.uniform(0, video_duration - audio_duration)

        # Calculate the dimensions for the 9:16 aspect ratio crop
        if width / height > 9 / 16:  # wider than 9:16, crop sides
            new_width = int(height * (9 / 16))
            new_height = height
        else:  # narrower than 9:16, crop top and bottom
            new_width = width
            new_height = int(width * (16 / 9))

        video = ffmpeg.input(backgroundVideoPath)
        audio = ffmpeg.input(ttsAudioPath)

        # Trim the video to match the length of the audio
        video = video.trim(start=start_time, end=start_time + audio_duration)
        video = video.setpts('PTS-STARTPTS')

        # Crop the video to the desired aspect ratio
        video = ffmpeg.filter_(video, 'crop', new_width, new_height)

        # Merge the video and audio together, and output to output_path
        output = ffmpeg.output(video, audio, outputVideoPath)

        # Overwrite the output file if it exists
        output = ffmpeg.overwrite_output(output)

        # Run the ffmpeg command
        ffmpeg.run(output)

        return outputVideoPath
