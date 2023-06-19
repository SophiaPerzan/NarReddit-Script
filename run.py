from os import environ as env
from dotenv import load_dotenv
from scraper import Scraper
from tts import TTS
from videoGen import VideoGenerator

load_dotenv()

# scraper = Scraper(env)
# post = scraper.getHotPosts()
# print("Scraped post: "+post[0])
#
# tts = TTS(env)
# audioFile = tts.createAudio(post[0], post[1])
# print("Created audio file: " + audioFile)

videoGen = VideoGenerator(env)
videoFile = videoGen.generateVideo(
    'background-videos/MCParkour.mp4', 'speech.mp3', 'output/output.mp4')
if (videoFile != False):
    print("Created output video file at: " + videoFile)
