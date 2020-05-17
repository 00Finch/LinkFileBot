import praw
import datetime
import time

reddit = praw.Reddit(client_id = '',
 client_secret = '',
  username = '',
   password = '',
    user_agent = '')

initialTime = time.time()

PhrasesToLookFor = []
MyReply = ""

for comment in reddit.subreddit('Test').stream.comments():
    if (initialTime <= comment.created_utc):
        if(any(x in comment.body.lower() for x in PhrasesToLookFor)):
            try:
                comment.reply(MyReply)
            except:
                print("\n!! failed due to timeout")
                pass
