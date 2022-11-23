import praw
import time

reddit = praw.Reddit('bot', user_agent='cs40')

subreddits = reddit.subreddit("Trumpvirus").top(limit=225)
for post in subreddits: 
    print('post title=', post.title)
    reddit.subreddit("cs40_2022fall").submit(title=post.title, url=post.url)
    time.sleep(10)


# subreddits: 
# /r/TrumpCriticizesTrump/
# /r/Trumpvirus/
# /r/TrumpHatesTheTroops/
# /r/america/

# need at least 200 submissions, number of submissions posted: 270+

