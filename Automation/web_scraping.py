import requests
import bs4

res = requests.get('https://www.amazon.in/Automate-Boring-Python-Albert-Sweigart/dp/1593275994')
print(res.raise_for_status())  # To check if there was any problem in downloading this web page

soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)  # Returns HTML code

price = soup.select('.slot-price')[0].getText()
print("Price of the book is "+price)