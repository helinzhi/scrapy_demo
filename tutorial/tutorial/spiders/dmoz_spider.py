import scrapy

class DmozSpider(scrapy.Spider):
    name="dmoz"
    allowed_domains = ["liaoxuefeng.com"]
    start_urls = ['http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000']

    def parse(self, response):
        titles = response.xpath("//ul[@class='uk-nav uk-nav-side']//a/text()").extract()
        for title in titles:
            print (title)