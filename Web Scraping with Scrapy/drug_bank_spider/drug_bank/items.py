# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DrugBankItem(scrapy.Item):
    page_url = scrapy.Field()
    db_drug_name = scrapy.Field()
    db_acc_num = scrapy.Field()
    db_drug_type = scrapy.Field()
    db_drug_group = scrapy.Field()
    # db_drug_description = scrapy.Field()
    # db_drug_category = scrapy.Field()
    db_cas_num = scrapy.Field()
    db_molecular_weight = scrapy.Field()
    # db_metabolism  = scrapy.Field()
    db_absorbtion = scrapy.Field()
    # db_vol_distribution = scrapy.Field()
    db_protein_binding = scrapy.Field()
    # db_clearance = scrapy.Field()
    db_affected_organisms = scrapy.Field()
    # db_adrs = scrapy.Field()
    db_synth_ref = scrapy.Field()
    db_num_manufacturers = scrapy.Field()
    db_num_packagers = scrapy.Field()
    db_num_dosage_forms = scrapy.Field()
    db_num_patents  = scrapy.Field()
    # db_melting_point = scrapy.Field()
    # db_water_solubility = scrapy.Field()
    # db_log_p = scrapy.Field()
    db_chem_state = scrapy.Field()
    db_kingdom = scrapy.Field()
    db_super_class = scrapy.Field()
    db_class = scrapy.Field()
    db_sub_class = scrapy.Field()
    db_molecular_framework = scrapy.Field()
    db_num_drug_interactions = scrapy.Field()
    db_drug_interactions_url = scrapy.Field()
    db_generic_names = scrapy.Field()
    db_generic_names_table_url = scrapy.Field()
    db_num_food_interactions = scrapy.Field()
    # db_ahfs_code = scrapy.Field()
    db_num_clin_trials = scrapy.Field()
    db_brand_names_table_url = scrapy.Field()
    db_brand_names = scrapy.Field()
    db_num_targets = scrapy.Field()
    db_mixture_products_table_url = scrapy.Field()
    db_mixture_names = scrapy.Field()
    pass
