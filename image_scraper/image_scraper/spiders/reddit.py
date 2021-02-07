import os
import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/']

    def parse(self, response):
        if self.is_logged_in(response):
            self.logger.debug("logged in!")
            scrapy.shell.inspect_response(response, self)
        else:
            return scrapy.Request(url="https://www.reddit.com/login", callback=self.log_in)

    def is_logged_in(self, response):
        if response.css("[href^='https://www.reddit.com/login']"):
            return False
        else:
            return True

    def log_in(self, response):
        self.logger.debug("going to try to log in...")
        try:
            # csrf_token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()
            destination = f'https://www.reddit.com/user/{os.environ["REDDIT_USERNAME"]}/saved'
            request = scrapy.FormRequest.from_response(
                response,
                # dont_click=True,
                clickdata= { 'type': 'submit' },
                method='POST',
                formdata={
                        'dest': destination,
                        'username': os.environ['REDDIT_USERNAME'],
                        'password': os.environ['REDDIT_PASSWORD'] #,
                        #'csrf_token': csrf_token
                        },
                callback=self.after_login
            )
            return request
        except KeyError:
            self.logger.error("REDDIT_USERNAME and REDDIT_PASSWORD environment variables must be set to use Reddit scraper.")

    def after_login(self, response):
        self.logger.debug("attempted login! lets see...")
        # scrapy.utils.response.open_in_browser(response)
        scrapy.shell.inspect_response(response, self)
