import webbrowser
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def titleprint(titl, b):
    if b == 1:
        base = "https://www.owasp.org"
    links = titl.findAll('a')
    href=[]
    for link,c in zip(links,list(range(0,len(links)))):
        title = link.get('title')
        href.append((urljoin(base,link.get('href'))))
        print("{}.   {}".format(c,title))
       	

    title_href=dict(zip(range(0,len(links)),href))
    choice=int(input("enter number:"))
    if (choice>len(links)):
        print("please enter number from 0 to ",len(links))
    else:
    	r=requests.get(title_href.get(choice))
    	webbrowser.open(title_href.get(choice))

a = input("Enter your search term:\n")
print("Search on?\n1. Owasp\n2. Wikipedia\n3. Youtube")

b = int(input("Enter number:"))
if (b == 1):
    search = "https://www.owasp.org/index.php?title=Special%3ASearch&profile=default&fulltext=Search&search={}"
    url = search.format(a)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    search_res = soup.find("ul", {"class": "mw-search-results"}).contents
    titl = BeautifulSoup(str(search_res), 'html.parser')
    titleprint(titl, b)
