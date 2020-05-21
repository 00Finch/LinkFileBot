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

        # if the comment isn't from the bot
        if(comment.author.name.strip() != privateInfo[2]):
            try:
                # grabs link from comment body
                linkIndex = comment.body_html.find("href")
                linkEndIndex = comment.body_html.find("\">http", linkIndex)
                link = comment.body_html[linkIndex + 6:linkEndIndex]

                # linkIndex will be -1 if no link is present in the comment
                if(linkIndex < 0):
                    continue

                # prints the link to the terminal
                print(link)

                text = ContentFinder.GenerateLinkDescription(link)

            except:
                continue

            comment.reply(text)

        else:
            continue


if __name__ == "__main__":
    main()
