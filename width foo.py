from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import sys
import time


global_wiki = 'https://en.wikipedia.org'
wiki_url = '/wiki/Special:Random'

def foo(first_article, second_article):
    mass = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{}}
    mass[0][first_article] = 'start_article'

    flag = 0
    all_links = set()
    for i in range(0,9):
        print ('lvl ' + str(i) + ' is working ' + str(time.time()/3600))
        print (len(mass[i]))
        for key in mass[i]:
            if (key not in all_links):
                all_links.add(key)
                try:
                    req = Request(key)
                    web_page = urlopen(req)
                    html_doc = web_page.read()
                    soup = BeautifulSoup(html_doc, "html.parser")
                except Exception as err:
                    print(err)
                    print(key)
                    continue
                for abzac in soup.find_all('p'):
                    for link in abzac.find_all('a'):
                        buffer = link.get('href')
                        if (str(buffer)[0:5] == '/wiki'):
                            mass[i+1][global_wiki + buffer] = web_page.geturl()
                            if (global_wiki + buffer == second_article):
                                print('Win' + str(i) + '!!!')
                                print(second_article)
                                rev = mass[i+1][second_article]
                                for a in range(i, -1, -1):
                                    print(rev)
                                    rev = mass[a][rev]
                                flag = 1
                                break
                    if flag:
                        break
            if flag:
                break
        if flag:
                break
            

#------------------------
a = 1
if (a == 0):
    first_article = ('https://en.wikipedia.org/wiki/The_Godfather')
    second_article = ('https://en.wikipedia.org/wiki/World_Bank')
else:
    first_article = global_wiki + wiki_url
    second_article = global_wiki + wiki_url

req = Request(first_article)
web_page = urlopen(req)

req2 = Request(second_article)
web_page2 = urlopen(req2)

print('Первая и вторая статьи')
first_article = (web_page.geturl())
second_article = (web_page2.geturl())


print (first_article)
print (second_article)
#-------------------------

print('Путь в одну сторону')
foo(first_article, second_article)
print('Путь в обратную сторону')
foo(second_article, first_article)
                
