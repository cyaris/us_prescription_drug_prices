# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodrxItem(scrapy.Item):
    # define the fields for your item here like:
    drug_url = scrapy.Field()
    grx_drug_warning = scrapy.Field()
    drug_name = scrapy.Field()
    generic_name = scrapy.Field()
    grx_lowest_price = scrapy.Field()
    grx_pharmacy = scrapy.Field()
    grx_purchase = scrapy.Field()
    grx_avg_cash_price = scrapy.Field()
    grx_fair_price = scrapy.Field()
    drug_notice = scrapy.Field()
    grx_over_counter = scrapy.Field()
    grx_popularity_rank = scrapy.Field()
    grx_competition_amount = scrapy.Field()
    grx_affordability_rank = scrapy.Field()
    grx_no_prices_found = scrapy.Field()
    grx_not_avail = scrapy.Field()
    pass
