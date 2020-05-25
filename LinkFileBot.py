import praw
import time
import ContentFinder
import LinkExtractor



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
    while True:
        for comment in reddit.subreddit('All').stream.comments(skip_existing=True):

            # if the comment isn't from the bot
            if(comment.author.name.strip() != privateInfo[2]):
                try:
                    # grabs link from comment body
                    link = LinkExtractor.ExtractLink(comment)
                    if not link: break

                    # prints the link to the terminal
                    print(f"||\n{link}\n||", flush=True)

                    text = ContentFinder.GenerateLinkDescription(link)

                except:
                    continue

                try:
                    comment.reply(text)
                    time.sleep(360)
                except Exception as e:
                    print(e, flush=True)
                    time.sleep(360) #sleep six minutes
                    break
            else:
                continue





if __name__ == "__main__":
    main()
