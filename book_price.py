import requests
from bs4 import BeautifulSoup
r = requests.get('https://search.books.com.tw/search/query/key/python/cat/all')

# print(r.text)

soup = BeautifulSoup(r.text,'html.parser')


################################## get the price of the book
attr = {"class": "price clearfix"}
price_tags = soup.find_all("ul", attrs= attr)

prices = []

for item in price_tags:
    t = item.get_text().strip()
    index_comma = t.find(",")
    index_dollar = t.find("元")
    
    if index_comma >= 0:
        price_str = t[index_comma+2 : index_dollar-1]
        prices.append(int(price_str))

print(prices)

print("average: " + str(sum(prices)/len(prices)))

################################## 


title_tags = soup.find_all('div', class_='box')

titles = []
links = []

for tag in title_tags:
    if 'title' in tag.a.attrs:
        book_link = "http:"+ tag.a['href']
        book_name = tag.a['title']
        if book_name == "Python" or book_name=="python":
            continue
        if book_name not in titles:
            titles.append(book_name)
            print(book_name)
        
        if book_link not in links:
            links.append(book_link)
            print(book_link)
      
    
print(len(prices))
print(len(links))

print(prices)

with open("book.csv","a",encoding = "utf-8") as f:
    for i in range(len(prices)):
        f.write(titles[i] + "," + str(prices[i]) + "," + links[i] + "\n") 
