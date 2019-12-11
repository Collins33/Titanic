from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):

    name = 'spiderform'

    start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

    def parse(self, response):
        # define form data we want to pass in
        formdata = {'firstname': 'Collins',
                    'lastname': 'Njau',
                    'jobtitle': 'Developer'}
        # return FormRequest from response object
        return FormRequest.from_response(response, formnumber=0, formdata=formdata, callback=self.after_post)

    def after_post(self, response):
        print("\n\n*************\nFORM PROCESSES.\n")
        print(response)
        print("\n\n*************\nFORM PROCESSES.\n")
