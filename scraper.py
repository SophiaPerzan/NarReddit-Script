import praw

class Scraper:
    def __init__(self, env):
        self.env = env
        self.hotPosts = []

        # Read-only instance
        self.reddit = praw.Reddit(client_id=env['CLIENT_ID'],
                            client_secret=env['CLIENT_SECRET'],
                            user_agent=env['USER_AGENT'])
        self.reddit.read_only = True
        self.subreddit = self.reddit.subreddit(env['SUBREDDIT'])
    
    def getHotPosts(self):
        for post in self.subreddit.hot():
            if not post.stickied and post.is_self and len(post.selftext) > 2000 and len(self.hotPosts) < 2:
                self.hotPosts.append(post)
            if len(self.hotPosts) >= 2:
                break
            
        self.hotPosts = self.hotPosts[:1]
        post = self.hotPosts[0]
        return post.title+" "+post.selftext