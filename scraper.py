import scrapy

class ScraperSet(scrapy.Spider):
    ''' Class responsible to create the Scraper Schema '''

    file = open('websites.txt', 'r', encoding="utf8")

    list_sites = [line.rstrip() for line in file]
    
    if len(list_sites) == 0:
        print("A lista de sites não está formatada corretamente, favor verificar")        

    else:
        print("Começou a leitura dos sites...")
        

    name = "test_spider"

    start_urls = list_sites


    def parse(self, response):
        '''Method responsible to get pseudoselectors'''
        SET_SELECTOR = '.header'

        for data in response.css(SET_SELECTOR):

            LOGO_SELECTOR = 'img ::attr(src)'

            PHONE_SELECTOR = 'a ::text'
           

            yield {
                # assembly of the yield with the first element of each selector
                'logo': data.css(LOGO_SELECTOR).extract_first(),
                'phones': data.css(PHONE_SELECTOR).extract_first(),
                'website': response.request.url ,
            }
