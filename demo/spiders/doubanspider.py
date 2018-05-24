from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from items import DoubanItem
from scrapy.http import Request


class Douban(CrawlSpider):
    name = "douban"
    start_urls = ['http://movie.douban.com/top250']

    url = 'http://movie.douban.com/top250'

    def parse(self, response):
        # print response.body
        item = DoubanItem()
        selector = Selector(response)
        # print selector
        Movies = selector.xpath('//div[@class="info"]')
        # print Movies
        for eachMoive in Movies:
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ''
                # print fullTitle
            # print movieInfo
            # print star
            # print quote
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo)
            item['star'] = star
            item['quote'] = quote
            yield item
            nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
            if nextLink:
                nextLink = nextLink[0]
                print nextLink
                yield Request(self.url + nextLink, callback=self.parse)