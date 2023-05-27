from os import environ as env
from dotenv import load_dotenv
from scraper import Scraper

load_dotenv()

scraper = Scraper(env)

post = scraper.getHotPosts()

