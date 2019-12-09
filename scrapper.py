from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')

divs = soup.find_all('div', {'class':'featured'})
# for div in divs:
#   print(div)


div = soup.find('div', {'class':'featured'})
print(div)

# chain with the h2 tag and get text without the tags
featured_header = soup.find('div', {'class':'featured'}).h2
print(featured_header.get_text())

# find attributes with class button button--primary
for button in soup.find(attrs={'class': 'button button--primary'}):
  print(button)

# find all hyperlinks
for link in soup.find_all('a'):
  print(link.get('href'))