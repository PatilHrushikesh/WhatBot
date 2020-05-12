import requests
from bs4 import BeautifulSoup as bs
#class Scraper:
#	def __init__(self):
markup = requests.get('https://majhinaukri.in/').text

soup = bs(markup, 'html.parser')

links = soup.findAll("h2", {"class": "post-box-title"})
mudat = "[मुदतवाढ]"
current = "(चालू घडामोडी)"
msgs = ""
for link in links:
    url = link.a["href"]
    link = str(link)
    start = link.find('/">') + 3
    end = link.find("</a>", start)
    msg = link[start:end]
    msg = msg + " " + url
    msgs = msgs + "\n\n" + msg

# if __name__ == "__main__":
#     print("News :" + msg)
#     print("Link :" + url)
#     print("-------------------")
