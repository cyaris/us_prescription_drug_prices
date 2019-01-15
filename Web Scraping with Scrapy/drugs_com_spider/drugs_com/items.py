# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugsComItem(scrapy.Item):
    # define the fields for your item here like:
    letter_url1 = scrapy.Field()
    letter_url2 = scrapy.Field()
    drug_url = scrapy.Field()
    drug_name = scrapy.Field()
    generic_name = scrapy.Field()
    brand_names = scrapy.Field()
    num_serious_interactions = scrapy.Field()
    num_common_side_effects = scrapy.Field()
    pregnancy_category = scrapy.Field()
    pass
