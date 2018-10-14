from scrapy.spiders import CrawlSpider, Rule
from risk.items import SummaryPostItem
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor
import scrapy

class PostLoader(ItemLoader):
    pass

class RiskSpider(CrawlSpider):
    name = 'risk'
    start_urls = [
        'https://www.risk.ru/blog?Topic_page=1'
    ]
    rules = (
        Rule(LinkExtractor(allow=('/blog\?Topic_page*', )), callback='parse_summary', follow=False),
    )

    def parse_summary(self, response):
        for post in response.css('div.commonPost'):
            item = SummaryPostItem()
            tag_names = post.css('div.rightPart div.postTags a::attr(data-type)').extract()
            tag_values = post.css('div.rightPart div.postTags a::text').extract()
            tags = {name: value for name, value in zip(tag_names, tag_values)}
            item['tag_activity'] = tags['activity'] if 'activity' in tag_names else None
            item['tag_place'] = tags['place'] if 'place' in tag_names else None
            item['tag_xtype'] = tags['xtype'] if 'xtype' in tag_names else None
            item['tag_group'] = tags['group'] if 'group' in tag_names else None
            item['tag_category'] = tags['category'] if 'category' in tag_names else None
            item['ID'] = post.css('div.header h2 a::attr(href)').extract_first()
            item['rating'] = post.css('div.ratingButtons div.number::text').extract_first()
            item['title'] = post.css('div.rightPart div.header h2 a::text').extract_first()
            item['author'] = post.css('div.author span.userInfo a::attr(href)').extract_first()
            item['date'] = post.css('div.rightPart span::text').extract_first().split(' ')[1]
            item['img'] = True if len(post.css('div.postBody img')) != 0 else False
            item['video'] = True if len(post.css('iframe.embed_video')) != 0 else False
            yield item   
        next_page = response.css('li.next a::attr(href)').extract_first()
       
        if next_page is not None: #and int(next_page.split('=')[-1]) < 1000:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse_summary)