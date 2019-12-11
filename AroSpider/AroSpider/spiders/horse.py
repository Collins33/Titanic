import scrapy

class HorseSpider(scrapy.Spider):

  #give it a unique name so that scrappy can know which spider to run
  name = 'tarantula'

  # defines initial request to be made
  # how to follow links
  def start_requests(self):
    # list of urls to process
    urls = ['https://treehouse-projects.github.io/horse-land/index.html', 'https://treehouse-projects.github.io/horse-land/mustang.html']
    
    # return a list
    return [scrapy.Request(url=url, callback=self.parse) for url in urls]
  
  # tell the spider how extracted data 
  # from start_requests will be parsed
  def parse(self, response):
    url = response.url # rep a response object from the request made in start_request
    page =  url.split('/')[-1]
    filename= 'horses-%s' % page
    print('URL is: {}'.format(url))
    with open(filename, 'wb') as file:
      file.write(response.body)
    print('Saved file %s' % filename)
