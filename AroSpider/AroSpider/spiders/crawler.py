from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Crawler(CrawlSpider):

    name = 'spiderman'

    # this sets the allowed domains
    # to prevent the spider from going out of control

    allowed_domains = ['treehouse-projects.github.io']

    # define a place to start
    start_urls = ['https://treehouse-projects.github.io/horse-land']

    # use LinkExtractor to define links to follow or ignore
    rules = [Rule(LinkExtractor(allow=r'.*'),
                  callback='parse_horses', follow=True)]

    # define parse_horses
    # takes self and response of the link extractor
    def parse_horses(self, response):
        # extract page url
        url = response.url
        # extract the text from the title
        page_title = response.css('title::text').extract()[0]
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(page_title))
