# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:53:41 2020

@author: Vilash
"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import StifelItem
from w3lib.html import remove_tags



class AdvisorSpider(CrawlSpider):
    name = 'advisor'
    
    start_urls = ['https://www.stifel.com/branch']
    
    rules = (
        Rule(LinkExtractor(restrict_css="ul.branch-landing-locations-list > li > a"), callback="scrapAdvisorInfo"),            
    )        
        
    def scrapAdvisorInfo(self, response):
        print("Working on: ", response.url)
        
        company_loader = ItemLoader(item=StifelItem(), response=response)
        company_loader.default_input_processor = MapCompose(remove_tags)
        company_loader.default_output_processor = TakeFirst()
        
        company_loader.add_value("page_url", response.url)
        company_loader.add_css("company_name", "h1.bold-headline")
        company_loader.add_css("branch_manager", "div.branch-landing-info-border div span a")
        company_loader.add_css("company_contact", "div.branch-landing-phone-desktop a")
        
        company_loader.add_css("company_address", "div.branch-landing-address")
        company_loader.add_css("company_advisor_urls", "div.branch-landing-financial-advisors-columns div.branch-landing-financial-advisors-branchFA a")
        
        yield company_loader.load_item()
        
