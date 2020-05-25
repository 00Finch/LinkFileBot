from bs4 import BeautifulSoup as bs
import re

def ExtractLink(comment):
    soup = bs(comment.body_html, 'lxml')
    link = (soup.select_one('a', attrs={'href': re.compile("^http://")}).text).strip()
    return(link)

def ExtractLinkP(comment):
    try:
        soup = bs(comment.body_html, 'lxml')
        link = (soup.select_one('a', attrs={'href': re.compile("^http://")}).text).strip()
        print(f"FOUND LINK: \n{link}\n", flush=True)
    except:
        print("FAILED", flush=True)
