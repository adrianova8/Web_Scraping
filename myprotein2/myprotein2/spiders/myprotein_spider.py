
import scrapy
from ..items import MyproteinItems
#import scrapy_fake_useragent

class MyproteinSpider(scrapy.Spider):
    name = 'myprotein_products'
    '''
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES' : {
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
            'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware' : 300,
        }
    }
    '''
    start_urls = ['https://www.myprotein.es/clothing/mens/sweatshirts-and-hoodies.list']
    

    def parse(self, response):
        items = MyproteinItems()

        hoodies = response.css('.athenaProductBlock')

        for hoodie in hoodies:
            title = hoodie.css('.athenaProductBlock_title h3::text').extract()
            price = hoodie.css('.athenaProductBlock_priceValue::text').extract()
            img = hoodie.css('.athenaProductBlock_image_rollover::attr(src)').extract()


            # Save the data
            items['title'] = title
            items['img'] = img
            items['price'] = price


            yield items
        

    '''
    def __init__(self, **kwargs):
        self.start_url = 'https://www.myprotein.es/clothing/mens/sweatshirts-and-hoodies.list'
        super().__init__(**kwargs)
    
    def requests(self):
        import requests
        from fake_useragent import UserAgent
        from scrapy.http import TextResponse

        # Iterate all pages
        headers = {'user-agent': UserAgent().Chrome}
        status_code = requests.get(self.start_urls, headers = headers)
        response = TextResponse(status_code.url, body = status_code.text, encoding = 'utf-8')
        urls = response.xpath('//*[@class="productListPorducts_products"]/li/div/div/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):

        item = MyproteinItems()
        
        item['title'] = response.xpath('//*[@class="productName_title"]/text()').extract()
        item['price'] = response.xpath('//*[@class="productPrice_price"]/text()').extract()
        item['img'] = response.xpath('//*[@class="athenaProductImageCarousel_image"]/@src').extract()
        item['link'] = response.url

        yield item
        '''

    
