import requests
from bs4 import BeautifulSoup as bs
import sys
import re
from nsfw import DetectSentence

'''
Call using GenerateLinkDescription(<link>)
Returns a string containing link description
If no description applicable returns False
'''
def GenerateLinkDescription(link):
    if (link[:2] in ["r/", "u/"] or link[:3] in ["/r/", "/u/"]):
        return False
        # print(link[:2])
        # return (f"Link leads to {link} on reddit.com")

    #establish webpage instance
    requestsInstance = requests.get(link)

    # espablish beautifulsoup instance
    soup = bs(requestsInstance.content, 'lxml')

    #Get link using beautifulsoup library
    try:
        title = (soup.select_one('title').text).strip()
        #ignore imgur default title and search again
        if title == 'Imgur: The magic of the Internet':
            return (GenerateLinkDescription(link))
        elif title.strip() == 'Google':
            return False
        else:
            return OrganizeDescription(title)
    except KeyboardInterrupt:
        raise
    except:
        pass

    # If beautifulsoup fails, attempt using regex
    try:
        # capture title using regex
        title = re.findall('<title>(.*?)</title>', str(requestsInstance.content))[0]
        # clean up title
        title = title.replace('\\n', '').strip()
        #ignore imgur default title and search again
        if title == 'Imgur: The magic of the Internet':
            return (GenerateLinkDescription(link))
        elif title.strip() == 'Google':
            return False
        else:
            return OrganizeDescription(title)
    except KeyboardInterrupt:
        raise
    except:
        pass

    #return false if no title found
    return False


def OrganizeDescription(title):
    nsfw = DetectSentence(title)
    if nsfw: retString = "## NSFW Warning\
    \n---------------\nit was detected that there is a high probability that \
the linked content contains material which may not be appropriate:\n\n"
    else: retString = "This link leads to:\n\n"
    if nsfw: retString += ">!"
    retString += title
    if nsfw: retString += "!< \n"
    if (title.count(' | ') > 0):
        splitTitle = title.rsplit(' | ')
        retString += "\n\n"
        if nsfw: retString += ">!"
        retString += "-- **"
        retString += splitTitle[1] + "**"
        if nsfw: retString += "!<"
    elif (title.count(' - ') > 0):
        splitTitle = title.rsplit(' | ')
        retString +="\n\n"
        if nsfw: retString += ">!"
        retString += "-- **"
        retString += splitTitle[1] + "**"
        if nsfw: retString += "!< "

    retString += "\n\n ^(I am a bot. This action was preformed automatically.)"

    return retString


'''
Run from commandline using command
python ContentFinder.py <link>
'''
if __name__ == "__main__":
    link = str(sys.argv[1])
    print(GenerateLinkDescription(link))
