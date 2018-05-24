from scrapy import cmdline

cmdline.execute("scrapy crawl douban -o items.csv -t csv".split())