import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qurl='https://books.toscrape.com/'

qheader={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

resp= rq.get(url= qurl,headers= qheader)

ab= BeautifulSoup(resp.content,'html.parser')

#print(ab)

def removeNavigablestring(list_data):
    return list(filter(lambda x: type(x) != NavigableString,list_data))

c1= removeNavigablestring(ab.ol.children)

#print(c1[0].children)

l = c1[4]

l= c1[4].h3.a.attrs['title']

print('Title 1 :-' , l )

print('////')
print('////')
print('////')
print('////')

l= c1[5].h3.a.attrs['title']

print('Title 2 :-' , l )

print('------')
print('------')
print('------')

l = c1[6].h3.a.attrs['title']

print('Title 3 :-' , l )

print('........')
print('........')
print('........')

l = c1[7].h3.a.attrs['title']

print('Title 4 :-' , l )