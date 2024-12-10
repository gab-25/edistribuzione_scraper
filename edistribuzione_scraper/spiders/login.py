import scrapy


class LoginSpider(scrapy.Spider):
    name = "login"
    allowed_domains = ["private.e-distribuzione.it"]
    start_urls = ["https://private.e-distribuzione.it/PortaleClienti/s/login"]

    def parse(self, response):
        pass
