# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LabelCollectItem(scrapy.Item):
    tag = scrapy.Field()
    labels = scrapy.Field()
    play_count = scrapy.Field()
    comment_count = scrapy.Field()
    collect_count = scrapy.Field()

