import ffmpeg
import os


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

        video = ffmpeg.input(backgroundVideoPath)
        audio = ffmpeg.input(ttsAudioPath)

        # Get the duration of the audio file
        probe = ffmpeg.probe(ttsAudioPath)
        audio_duration = float(probe['streams'][0]['duration'])+2

        # Trim the video to match the length of the audio
        video = ffmpeg.filter_(video, 'trim', duration=audio_duration)

        # Merge the video and audio together, and output to output_path
        output = ffmpeg.output(video, audio, outputVideoPath)

        # Overwrite the output file if it exists
        output = ffmpeg.overwrite_output(output)

        # Run the ffmpeg command
        ffmpeg.run(output)

        return outputVideoPath
