import requests
import bs4

result = requests.get("https://www.example.com")
print(type(result))
#print(result.text)
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

import requests
import bs4

result = requests.get("https://www.example.com")
print(type(result))
#print(result.text)
soup = bs4.BeautifulSoup(result.text,'lxml')
print(soup)

print(soup.select("title")[0].getText())  # provide only content ( not tags )
print(soup.select("p"))
print(soup.select("h1"))
print(soup.select("p"))