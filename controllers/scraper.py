import scrapy

class TestSet(scrapy.Spider):
    ''' '''

    file = open('websites.txt', 'r', encoding="utf8")

    listsites = [line.rstrip() for line in file]
    
    if len(listsites) == 0:
        print("A lista de sites não está formatada corretamente, favor verificar")        

    else:
        print("Começou a leitura dos sites...")
        

    name = "test_spider"

    start_urls = listsites


    def parse(self, response):

        SET_SELECTOR = '.header'

        for data in response.css(SET_SELECTOR):

            LOGO_SELECTOR = 'img ::attr(src)'

            PHONE_SELECTOR = 'a ::text'
            # PHONE_SELECTOR = '//*[contains(text(), "465-9555")]'

            yield {
                # montagem do Yield com primeiro elemento de cada seletor
                'logo': data.css(LOGO_SELECTOR).extract_first(),
                'phones': data.css(PHONE_SELECTOR).extract_first(),
                'website': response.request.url ,
            }
