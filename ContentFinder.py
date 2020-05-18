import requests
from bs4 import BeautifulSoup as bs
import sys
import re


'''
Call using GenerateLinkDescription(<link>)
Returns a string containing link description
If no description applicable returns False
'''
def GenerateLinkDescription(link):
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
         else:
             return title
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
        else:
            return title
    except KeyboardInterrupt:
        raise
    except:
        pass

    #return false if no title found
    return False


'''
Run from commandline using command
python ContentFinder.py <link>
'''
if __name__ == "__main__":
    link = str(sys.argv[1])
    print("\n\n Title:\n {}\n\n".format(GenerateLinkDescription(link)))
