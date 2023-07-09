from os import environ as env
from dotenv import load_dotenv
from scraper import Scraper
from tts import TTS
from videoGen import VideoGenerator
import os
from gpt import GPT

load_dotenv()

scraper = Scraper(env)
post = scraper.getHotPosts()
postTitle = post[0]
postTitleAndText = post[1]
print("Scraped post: "+postTitleAndText)

gpt = GPT(env)
gender = gpt.getGender(postTitleAndText)
editedPost = gpt.expandAcronymsAndAbbreviations(postTitleAndText)

tts = TTS(env)
audioFile = tts.createAudio(editedPost, gender)
print("Created audio file: " + audioFile)

videoGen = VideoGenerator(env)
directory = 'background-videos'
outputPath = os.path.join('output', 'output.mp4')
bgVideoFileName = env['BG_VIDEO_FILENAME']
videoFile = videoGen.generateVideo(
    bgVideoFileName, audioFile, outputPath, directory)
if (videoFile != False):
    print("Created output video file at: " + videoFile)
else:
    print("Failed to create output video file")
