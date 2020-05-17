import requests
from bs4 import BeautifulSoup as bs
import sys

def GenerateLinkDescription(link):
    requestsInstance = requests.get(link)
    soup = bs(requestsInstance.content, 'lxml')
    return (soup.select_one('title').text)

link = sys.argv[1]

print("\n\n Title:\n{}\n\n".format(GenerateLinkDescription(link)))
