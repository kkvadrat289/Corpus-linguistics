import scrapy

class SummaryPostItem(scrapy.Item):
    ID = scrapy.Field()
    rating = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    img = scrapy.Field()
    video = scrapy.Field()
    tag_activity = scrapy.Field()
    tag_place = scrapy.Field()
    tag_group = scrapy.Field()
    tag_category = scrapy.Field()
    tag_xtype = scrapy.Field()
    
class FullPostItem(scrapy.Item):
    ID = scrapy.Field()
    text1 = scrapy.Field()
    text2 = scrapy.Field()