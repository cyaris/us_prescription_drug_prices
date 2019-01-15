# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PharmacyCheckerItem(scrapy.Item):
    # define the fields for your item here like:
    pc_drug_url = scrapy.Field()
    drug_name = scrapy.Field()
    pc_dose_size = scrapy.Field()
    pc_lowest_price_per_unit = scrapy.Field()
    pc_lowest_price = scrapy.Field()
    pc_purchase_size = scrapy.Field()
    pc_online_pharmacy = scrapy.Field()
    pc_not_offered = scrapy.Field()
    generic_name = scrapy.Field()
    pass
