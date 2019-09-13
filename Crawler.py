import scrapy
from ..items import FirstspyderItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import Spider
from w3lib.html import remove_tags
from scrapy_splash import SplashRequest


class MySpider(Spider):
    name = 'Pipper'
    start_urls = ['https://www.decolar.com/shop/flights/search/roundtrip/GRU/FOR/2019-09-30/2019-10-07/1/0/0/NA/NA/NA/NA/NA/?from=SB&di=1-0'] #FIRST LEVEL

    def start_requests(self):


        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    # 1. SCRAPING
    def parse(self, response):

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



