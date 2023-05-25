import praw
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

# Read-only instance
reddit = praw.Reddit(client_id=env['CLIENT_ID'],
                     client_secret=env['CLIENT_SECRET'],
                     user_agent=env['USER_AGENT'])
reddit.read_only = True

subreddit = reddit.subreddit('AITAH')

hotPosts = []

for post in subreddit.hot():
    if not post.stickied and post.is_self and len(post.selftext) > 2000 and len(hotPosts) < 3:
        hotPosts.append(post)

hotPosts = hotPosts[:1]

print()
for post in hotPosts:
    print()
    print(post.score, ": ", post.title)
    print(post.selftext)
