# -*- coding: utf-8 -*-
import scrapy


class NewmovieSpider(scrapy.Spider):
    name = 'newmovie'
    allowed_domains = ['dytt.com']
    start_urls = ['http://www.dytt8.net/']

    def parse(self, response):
        for each in response.xpath("//div[@class='co_content8']"):
            item[name] = each.xpath('td[1]/a/text()').extract()[0]
            item[link] = each.xpath('td[1]/a/@href').extract()[0]
            item[date] = each.xpath('td[2]/a/text()').extract()[0]

            yield item

