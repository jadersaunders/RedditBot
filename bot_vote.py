import praw
from textblob import TextBlob 

reddit = praw.Reddit('bot', user_agent='cs40')

# submission_text = TextBlob(submission.title)

# Your code must run on at least 100 submissions and all of the comments within those submissions (up to 500 comments total per submission) for the full extra credit. 
# Not all of these submissions/comments need to be upvoted if they do not match your particular criteria for voting.
# extra credit: upvoting candidate in favor of or downvoting candidate you oppose 

upvote_candidate = 'biden' 
# downvote_candidate = 'trump'
numbercommentupvoted = 0
numberupvoted = 0
numbercommentdownvoted = 0
numberdownvoted = 0

subreddits = reddit.subreddit("cs40_2022fall").hot(limit=None)

for post in subreddits: 
    if upvote_candidate in post.title.lower():
        content=TextBlob(str(post.title))
        if content.sentiment.polarity>0.5:
            post.upvote()
            numberupvoted+=1
            print('upvoted title=', post.title)
            print('number upvoted=', numberupvoted)
        else: 
            if content.sentiment.polarity<-0.5: 
                post.downvote()
                numberdownvoted+= 1
                print('downvoted title=', post.title)
                print('numberdownvoted=', numberdownvoted)
    post.comments.replace_more(limit=None)

# if ('biden' in text.lower() and text.sentiment.polarity>0.5) or ('trump' in text.lower() and text.sentiment.polarity<-0.5):
#     comment.upvote()
# else: 
#     if ('biden' in text.lower() and text.sentiment.polarity<-0.5) or ('trump' in text.lower() and text.sentiment.polarity>0.5):
#     comment.downvote()

    for reply in post.comments.list():
        text = TextBlob(str(reply.body))
        if upvote_candidate in reply.body.lower() and text.sentiment.polarity>0.5:
            reply.upvote()
            numbercommentupvoted += 1
            print('upvoted comment=', reply.body)
            print('number comment upvoted=', numbercommentupvoted)
        else: 
            if upvote_candidate in reply.body.lower() and text.sentiment.polarity<-0.5:
                reply.downvote()
                numbercommentdownvoted += 1
                print('downvoted comment=', reply.body)
                print('number comment downvoted=', numbercommentdownvoted)

print('========================================')
print('number upvoted=', numberupvoted)
print('========================================')
print('numberdownvoted=', numberdownvoted)
print('========================================')
print('number comment upvoted=', numbercommentupvoted)
print('========================================')
print('number comment downvoted=', numbercommentdownvoted)
print('========================================')


# blob = TextBlob(text)
# blob.tags 

# for sentence in blob.sentences: 
#     print(sentence.sentiment.polarity)

# sentence = TextBlob("")
# sentence.sentiment
# sentence.sentiment.polarity

# blob=TextBlob("")
# blob.classify()


