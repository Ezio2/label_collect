# -*- coding: utf-8 -*-
import scrapy
import urlparse


class YoukuSpider(scrapy.Spider):
    name = "youku"
    allowed_domains = ["youku.com"]
    start_urls = (
        'http://www.youku.com/v_showlist/c0.html',
    )

    def parse(self, response):
        for s in response.xpath("//div[@class='item item-moreshow']/ul/li/a"):
            for relative_path, tag in zip(s.xpath("@href").extract(), s.xpath("text()").extract()):
                url = urlparse.urljoin(response.url, relative_path)
                yield scrapy.Request(url=url, callback=self.search_all_labels,
                                     meta={"tag": tag, "label": [tag]})

    def search_all_labels(self, response):
        meta = response.meta
        for s in response.xpath("//div[@class='item']/ul/li/a/").extract():
            for url, label in zip(
                s.xpath("@href").extract(),
                s.xpath("@text").extract()
            ):
                yield scrapy.Request
