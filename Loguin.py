from scrapy.spiders import Spider
from scrapy.http import FormRequest
from w3lib.html import remove_tags
from scrapy_splash import SplashRequest


class MySpider(Spider):
    name = 'loguin'
    start_urls = ['https://quotes.toscrape.com/login']  # FIRST LEVEL

    # 1. SCRAPING
    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'fabiosouzao13@gmail.com',
            'password': 'sdasdas'
        },callback = self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
        items = FirstspyderItem()

        containers = response.css('div.cluster-container.COMMON')

        for flight in containers:
            price = flight.css('.price-amount::text')[0].extract()
            trip = flight.css('.stops-text::text')[0].extract()
            test = flight.css('span.best-duration::text')[0].extract()

            items['price'] = price
            items['trip'] = trip
            items['test'] = test

            yield items

