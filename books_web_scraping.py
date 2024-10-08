import requests
import bs4

# Goal : To grab a Title of every 2 star rating book

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

two_star_title = []

for n in range(1,51):
    scrap_url = base_url.format(n)
    res = requests.get(scrap_url)
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_title.append(book_title)

print(two_star_title)

