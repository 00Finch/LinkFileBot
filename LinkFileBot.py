import praw
import time
import ContentFinder



def main():

    accountFile = open("./exclude/account.txt", "r")
    privateInfo = []
    for i in range(0,4):
        privateInfo.append(accountFile.readline().rstrip())

    accountFile.close()

    reddit = praw.Reddit(client_id = privateInfo[0],
                         client_secret = privateInfo[1],
                         username = privateInfo[2],
                         password = privateInfo[3],
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
