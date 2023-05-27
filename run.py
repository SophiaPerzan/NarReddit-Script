from os import environ as env
from dotenv import load_dotenv
from scraper import Scraper
from tts import TTS

load_dotenv()

scraper = Scraper(env)
post = scraper.getHotPosts()
print("Scraped post: "+post[0])

tts = TTS(env)
tts.createAudio(post[0], post[1])
print("Created audio file")