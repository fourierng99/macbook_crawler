import scrapy
from selenium import webdriver
from scrapy.http import TextResponse


class Lazada(scrapy.Spider):
    name = "lazada"
    allowed_domains = ['lazada.vn']
    start_urls = ['http://www.lazada.vn/dien-thoai-may-tinh-bang/?ref=MT']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)
        page = TextResponse(
            response.url, body=self.driver.page_source, encoding='utf-8')
        required_data = page.xpath(
            '//div[contains(@class,"c1_t2i")]').extract()

        self.driver.close()
