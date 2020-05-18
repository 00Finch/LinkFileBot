import praw
import datetime
import time



accountFile = open("./exclude/account.txt", "r")
privateUsername = accountFile.readline().rstrip()
privatePassword = accountFile.readline().rstrip()
accountFile.close()

reddit = praw.Reddit(client_id = 'mquSmzl3A6nnSg',
 client_secret = 'ayz-KjEA2SkzCENTS5RvTaRpf24',
  username = privateUsername,
   password = privatePassword,
    user_agent = 'Link identification script (by /u/failcrab)')

# skip_existing=True skips any comments that were posted before the stream
# was created
"""
for comment in reddit.subreddit('Test').stream.comments(skip_existing=True):
    if(any(x in comment.body.lower() for x in PhrasesToLookFor)):
        try:
            comment.reply(MyReply)
        except:
            print("\n!! failed due to timeout")
            pass
"""
#skip_existing=True
counter = 0
for comment in reddit.subreddit('Test').stream.comments(skip_existing=True):
    try:
        print("HTML BODY: " + comment.body_html + "\n")
        linkIndex = comment.body_html.find("href")
        linkEndIndex = comment.body_html.find("\">http", linkIndex)
        link = comment.body_html[linkIndex + 6:linkEndIndex]
        print(link)
    except:
        continue
