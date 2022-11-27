import praw
import random
import datetime
import time
import markovify

madlibs = [
    "Trump [LOVES] thinking big about [LOTS] of things.  He learns from his [PAST] and [FOCUSES] the [PRESENT] while planning for the [FUTURE].",
    "Trump [CLAIMS] that he is [VERY] [RESPECTFUL] women.  He [SHOWED] his [TREMENDOUS] respect for women by wishing everyone a happy International Women's Day.  He also said that [NOBODY] has more respect for women than he does.",
    "Trump [WANTS] to build a [WALL], [SEPARATING] Mexico from the US.  He [THINKS] that this is [VITAL] to Make America [GREAT] again.",
    "Trump thinks that [LUCK] is [VITAL] to [SUCCESS].  However, he also [SAYS] that he [STARTED] with a [SMALL] loan of a million dollars.",
    "Trump [CLAIMS] that there is [NOBODY] who has [CONTRIBUTED] as much to [EQUALITY] as he has.  But he also [SAYS] that putting a wife to work is a very [DANGEROUS] thing.",
    "Trump is [CONVINCED] that his [IQ] is one of the [HIGHEST], and that [EVERYONE] knows it.  He [BELIEVES] that he is [VERY] intelligent."
    ]

replacements = {
    'LOVES' : ['loves', 'adores', 'likes'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'PAST' : ['past', 'prior experiences', 'preceding days', 'former decisions'], 
    'FOCUSES' : ['focuses','targets', 'centers his attention on', 'concentrates ', 'fixates on'], 
    'PRESENT' : ['present', 'current moment', 'present moment', 'here and now'], 
    'FUTURE' : ['future', 'impending days', 'days to come', 'imminent future'],
    'CLAIMS' : ['claims', 'asserts', 'declares', 'believes'], 
    'VERY' : ['very', 'extremely', 'incredibly', 'remarkably'],
    'RESPECTFUL': ['respectful of', 'gracious to', 'polite to'],
    'SHOWED': ['showed', 'demonstrated', 'displayed'],
    'TREMENDOUS': ['tremendous', 'incredible', 'extreme'],
    'NOBODY':['no one', 'nobody', 'zero people'],
    'WANTS':['wants', 'desires', 'aims'],
    'WALL':['wall', 'barrier', 'barricade', 'fence'],
    'SEPARATING':['separating', 'dividing', 'isolating'],
    'THINKS':['thinks', 'believes', 'is convinced'],
    'VITAL':['vital', 'extremely important', 'neccessary'],
    'GREAT':['great', 'amazing', 'fabulous', 'awesome'],
    'LUCK':['luck','chance','good fortune','good karma'],
    'SUCCESS':['success','happiness','achievements','victory','triumph'],
    'SAYS':['says', 'disclosed', 'reports'],
    'DANGEROUS': ['dangerous', 'scary', 'precarious', 'nasty', 'treacherous'],
    'STARTED':['started', 'began', 'initiated his career'],
    'SMALL':['small', 'minimal', 'miniscule', 'wee'],
    'CONTRIBUTED':['contributed', 'added to', 'increased', 'improved'],
    'EQUALITY': ['equality', 'equal rights', 'fair treatment'],
    'CONVINCED': ['convinced', 'sure', 'confident'],
    'IQ':['IQ', 'intelligence', 'knowledge'],
    'HIGHEST':['highest', 'best', 'greatest'],
    'EVERYONE':['everyone', 'everybody', 'all people'],
    'BELIEVES':['believes', 'concludes', 'supposes', 'thinks'],
    }

# FIXME:
# copy your generate_comment function from the madlibs assignment here

def generate_comment():
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot', user_agent='cs40')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://www.reddit.com/r/cs40_2022fall/comments/ywivox/project_4_reddit/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    # all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list() 

    with open(r"/Users/jadesaunders/Desktop/jadersaunders.github.io/trumptext.txt", encoding="utf-8") as f: 
# text = trump's inagural address (https://www.politico.com/story/2017/01/full-text-donald-trump-inauguration-speech-transcript-233907)
        text = f.read()

    with open(r"/Users/jadesaunders/Desktop/jadersaunders.github.io/trumptext2.txt", encoding="utf-8") as f: 
# text2 = trump campaign speech in wisconsin (https://www.politico.com/story/2016/08/full-text-donald-trumps-speech-on-227095)
        text += f.read()

    with open(r"/Users/jadesaunders/Desktop/jadersaunders.github.io/trumptext3.txt", encoding="utf-8") as f: 
# text 3 = trump farewell address (https://www.rev.com/blog/transcripts/president-donald-trump-farewell-address-speech-transcript)
        text += f.read()

    combined_model=''
    text_model1A = markovify.Text(text)

    # print 5 randomly generated sentences 
    for i in range(5): 
        combined_model += ' ' + str(text_model1A.make_sentence(tries=200)) 
    print('combined_model=', combined_model)

    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments: 
        if str(comment.author)!='llamabot45':
            not_my_comments.append(comment)

    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message

        text = generate_comment()
        submission.reply(text)
        time.sleep(5)

        # # text = generate_comment()
        # submission.reply(combined_model)
        # time.sleep(5)

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []

        for comment in not_my_comments: 
            replied = False 
            for reply in list(comment.replies):
                if str(reply.author)=='llamabot45':
                    replied = True 
            if replied == False: 
                comments_without_replies.append(comment)

        # extra credit: replying to most highly upvoted comment 
        # scores=comment.score, return scores 
        number_of_upvotes=0
        highly_upvoted_comments_without_replies = []
        for comment in comments_without_replies:
            if comment.score>number_of_upvotes:
                highly_upvoted_comments_without_replies=[comment]
                number_of_upvotes = comment.score
            else: 
                if comment.score == number_of_upvotes:
                    highly_upvoted_comments_without_replies.append(comment)

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message

        if len(comments_without_replies)>0:
            try: 
                random.choice(comments_without_replies).reply(generate_comment())
                comment.reply(combined_model)
            except praw.exceptions.APIException: 
                print('sleeping for 5 seconds')
                time.sleep(5)

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.

    subreddit = reddit.subreddit("cs40_2022fall")
    hot = list(subreddit.hot(limit=5))
    submission=random.choice(hot)

    pass
    time.sleep(5)
