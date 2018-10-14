from scrapy.spiders import CrawlSpider, Rule
from risk.items import FullPostItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
import scrapy

class PostLoader(ItemLoader):
    pass

class FullPostSpider(CrawlSpider):
    name = 'risk_post'
    start_urls = [
        'https://www.risk.ru/blog?Topic_page=1'
    ]
    rules = (
        Rule(LinkExtractor(allow=('/blog\?Topic_page*', )), callback='parse_summary', follow=False),
    )
    
    def parse(self, response):
        for href in response.css('div.header h2 a::attr(href)').extract():
            next_page = response.urljoin(href)
            yield scrapy.Request(next_page, callback=self.parse_post)
            
        next_page = response.css('li.next a::attr(href)').extract_first()
       
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
    
    def parse_post(self, response):
        item = FullPostItem()
        item['ID'] = '/' + '/'.join(response.url.split('/')[-2:] )
        item['text1'] = response.css('div.postBody p::text').extract()
        item['text2'] = response.css('div.postBody::text').extract()
        yield item