import scrapy


class Img1Spider(scrapy.Spider):
    name = "img1"
    allowed_domains = ["www.geeksforgeeks.org"]
    start_urls = ["https://www.geeksforgeeks.org/courses"]

    def parse(self, response):
        pass
