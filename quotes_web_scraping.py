import requests
import bs4

base_url = 'https://quotes.toscrape.com/page/'
page_still_valid = True
authors = set()
page = 1

while page_still_valid:
    page_url = base_url + str(page)

    res = requests.get(page_url)

    if 'No quotes found!' in res.text:
        break

    soup = bs4.BeautifulSoup(res.text,'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

    page+=1

print(authors)
