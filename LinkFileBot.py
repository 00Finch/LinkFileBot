import praw
import time
import ContentFinder



def main():

    accountFile = open("./exclude/account.txt", "r")
    privateUsername = accountFile.readline().rstrip()
    privatePassword = accountFile.readline().rstrip()
    accountFile.close()

    reddit = praw.Reddit(client_id = 'mquSmzl3A6nnSg',
     client_secret = 'ayz-KjEA2SkzCENTS5RvTaRpf24',
      username = privateUsername,
       password = privatePassword,
        user_agent = 'Link identification script (by /u/LinkFileBot)')

    # skip_existing=True skips any comments that were posted before the stream
    # was created
    for comment in reddit.subreddit('Test').stream.comments(skip_existing=True):
        try:
            # grabs link from comment body
            linkIndex = comment.body_html.find("href")
            linkEndIndex = comment.body_html.find("\">http", linkIndex)
            link = comment.body_html[linkIndex + 6:linkEndIndex]
            print(link)

            text = ContentFinder.GenerateLinkDescription(link)
            comment.reply(text)

        except:
            continue



main()
