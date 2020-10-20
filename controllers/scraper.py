import scrapy

class TestSet(scrapy.Spider):

    name='test_spider'

    start_urls = ["http://folhavponline.com.br/categoria/ultimas-noticias/"]

    def parse_data(self, response):

        SET_SELECTOR = '.MEDIA'

        for data in response.css(SET_SELECTOR):

            LOGO_SELECTOR = 'img ::attr(src)'
        
            TITLE_SELECTOR = 'a ::text'

            PHONE_SELECTOR= '//div["@class="date-created item"]/a/text()'

            yield {
                'logo': data.css(LOGO_SELECTOR).extract_first(),
                'phone': data.xpath(PHONE_SELECTOR).extract_first(),
                'site': data.css(TITLE_SELECTOR).extract_first(),
            }

            NEXT_PAGE_SELECTOR = '.page-numbers a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # print("AQUIII",next_page)
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )

        