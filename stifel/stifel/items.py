# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class StifelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_url = scrapy.Field()
    company_name = scrapy.Field()
    branch_manager = scrapy.Field()
    company_contact = scrapy.Field()
    company_address = scrapy.Field()
    company_advisor_urls = scrapy.Field()
    