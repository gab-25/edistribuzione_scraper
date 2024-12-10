import scrapy


class CurvedicaricoSpider(scrapy.Spider):
    name = "curvedicarico"
    allowed_domains = ["private.e-distribuzione.it"]
    start_urls = ["https://private.e-distribuzione.it/PortaleClienti/s/curvedicarico"]

    def parse(self, response):
        pass
