from urllib.request import urlopen
from bs4 import BeautifulSoup

import re

site_links = []
def internal_links(url):
  html = urlopen('https://treehouse-projects.github.io/horse-land/{}'.format(url))
  # create beautiful soup object
  soup = BeautifulSoup(html, 'html.parser')
  # return link of soup object
  return soup.find('a', href=re.compile('(.html)$'))



if __name__ == '__main__':
  urls = internal_links('index.html')
  # if it finds a link
  while len(urls) > 0:
    # find the href attribute
    page_href = urls.attrs['href']
    if page_href not in site_links:
      site_links.append(page_href)
      print(page_href)
      print('\n===============\n')
      urls = internal_links(page_href)
    else:
      break