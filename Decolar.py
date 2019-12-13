from scrapy.spiders import Spider
from ..items import FlightsItem
from scrapy_splash import SplashRequest
import pandas as pd

f = pd.read_excel("C:\\Users\\99797279\\PycharmProjects\\Spyder\\FlightCrawler\\Aereo Origem Destino.xlsx", "Sheet1")

f.rename(columns = {'Origem Destino':'Origem_destino'},inplace=True)

links = []

DiaInicial = "13"
MesInicial = "01"
AnoInicial = "2020"
DiaFinal = "25"
MesFinal = "01"
AnoFinal = "2020"

dataida = AnoInicial + "-" + MesInicial + "-" + DiaInicial
datavolta = AnoFinal + "-" + MesFinal + "-" + DiaFinal

for index, row in f[:30].iterrows():
    Org = row['Origem'][:3]
    Dest = row['Destino'].split("|")[-1][:3]
    linkdecolar = "https://www.decolar.com/shop/flights/search/roundtrip/" + Org + "/" + Dest + "/" + dataida + "/" + datavolta + "/1/0/0/NA/NA/NA/NA/NA/?from=SB&di=1-0"
    links.append(linkdecolar)

print(links)

class MySpider(Spider):
    name = 'Decolar'
    start_urls = links #FIRST LEVEL

    def start_requests(self):

        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={"wait": 3})

    # 1. SCRAPING
    def parse(self, response):
            items = FlightsItem()


            containers = response.css('div.cluster-container.COMMON')

            for flight in containers:
                Origem = flight.css('.airport span::text')[0].extract()
                Destino = flight.css('.airport span::text')[1].extract()
                price = response.css('.price-best .price-amount::text')[0].extract()
                trip = flight.css('.stops-text::text')[0].extract()
                test = flight.css('.name span::text')[0].extract()
                site = response.url

                items['Origem'] = Origem
                items['Destino'] = Destino
                items['price'] = price
                items['trip'] = trip
                items['test'] = test
                items['site'] = site

            yield items
