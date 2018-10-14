# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from risk.items import FullPostItem

class RiskPipeline(object):
    def process_item(self, item, spider):
        print("PIPELINE")
        if isinstance(item, FullPostItem):
            filename = item["ID"][1:].replace('/', '-')
            with open(filename + ".txt", "w") as f:
                f.write("".join(item["text1"]) + "".join(item["text2"]))
        return item
