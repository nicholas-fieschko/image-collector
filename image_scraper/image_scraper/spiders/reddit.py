import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def parse(self, response):
        pass
