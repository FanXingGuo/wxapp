# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=.+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'),callback="parse_detial",follow=False)
    )

    def parse_detial(self, response):
        title=response.xpath("//h1[@class='ph']/text()").get()
        author=response.xpath("//p[@class='authors']//a/text()").get()
        content=response.xpath('//td[@id="article_content"]//text()').getall()
        content="".join(content).split()

        item=WxappItem(title=title,author=author,content=content)
        yield item

