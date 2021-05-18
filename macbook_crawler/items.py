import scrapy

class DemoScrapyItem(scrapy.Item):
    product_name = scrapy.Field()
    price_sale =scrapy.Field()
    price = scrapy.Field()
    rate_average = scrapy.Field()
    params_cpu = scrapy.Field()
    params_vga = scrapy.Field()
    params_dr = scrapy.Field()
    url = scrapy.Field()