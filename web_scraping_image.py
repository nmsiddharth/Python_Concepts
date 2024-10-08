import requests
import bs4

res = requests.get("https://en.wikipedia.org/wiki/Virat_Kohli")

soup = bs4.BeautifulSoup(res.text,'lxml')

comp = soup.select('.mw-file-element')[0]
print(comp['src'])

image_link = requests.get("https://upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png")

print(image_link.content)

f = open("sid.png",'wb')
f.write(image_link.content)
f.close()


# Image is copyrighted , so not visible in sid.png