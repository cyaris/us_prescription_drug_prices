import scrapy
from pharmacy_checker.items import PharmacyCheckerItem

class PharmacyChecker(scrapy.Spider):
    name = 'pharmacy_checker'
    allowed_domains = ['pharmacychecker.com']
    start_urls = [
    'https://www.pharmacychecker.com/drug-prices/a/',
    'https://www.pharmacychecker.com/drug-prices/b/',
    'https://www.pharmacychecker.com/drug-prices/c/',
    'https://www.pharmacychecker.com/drug-prices/d/',
    'https://www.pharmacychecker.com/drug-prices/e/',
    'https://www.pharmacychecker.com/drug-prices/f/',
    'https://www.pharmacychecker.com/drug-prices/g/',
    'https://www.pharmacychecker.com/drug-prices/h/',
    'https://www.pharmacychecker.com/drug-prices/i/',
    'https://www.pharmacychecker.com/drug-prices/j/',
    'https://www.pharmacychecker.com/drug-prices/k/',
    'https://www.pharmacychecker.com/drug-prices/l/',
    'https://www.pharmacychecker.com/drug-prices/m/',
    'https://www.pharmacychecker.com/drug-prices/n/',
    'https://www.pharmacychecker.com/drug-prices/o/',
    'https://www.pharmacychecker.com/drug-prices/p/',
    'https://www.pharmacychecker.com/drug-prices/q/',
    'https://www.pharmacychecker.com/drug-prices/r/',
    'https://www.pharmacychecker.com/drug-prices/s/',
    'https://www.pharmacychecker.com/drug-prices/t/',
    'https://www.pharmacychecker.com/drug-prices/u/',
    'https://www.pharmacychecker.com/drug-prices/v/',
    'https://www.pharmacychecker.com/drug-prices/w/',
    'https://www.pharmacychecker.com/drug-prices/xyz/']

    def parse(self, response):
        root_domain = 'https://www.pharmacychecker.com'
        drugs = response.xpath('//*[@id="sidebar-layout"]/div[2]/section/ul/li/span[1]/a/@href').extract()
        while len(drugs)!=0:
            item = PharmacyCheckerItem()
            item['pc_drug_url'] = root_domain + drugs[0].strip("[,]'") + '?sort=cost_per_unit'
            request = scrapy.Request(item['pc_drug_url'], callback = self.parseDrugData)
            request.meta['PharmacyCheckerItem'] = item
            del(drugs[0])
            yield request

    def parseDrugData(self, response):
        item = response.meta['PharmacyCheckerItem']
        item = self.getDrugInfo(item, response)
        return item

    def getDrugInfo(self, item, response):
        item['drug_name'] = response.xpath('/html/body/div[2]/div/header/h1/text()').extract()
        try:
            item['pc_dose_size'] = str(response.xpath('/html/body/div[2]/div/header/h2/text()').extract())[12:-53]
        except:
            item['pc_dose_size'] = None
        try:
            item['pc_purchase_size'] = str(str(response.xpath('/html/body/div[2]/div').extract()).split('drug-pricing-details">')[1]).split('<')[0]
        except:
            item['pc_purchase_size'] = None
        try:
            item['pc_lowest_price_per_unit'] = response.xpath('/html/body/div[2]/div/section[3]/ul/li[1]/div[1]/div[3]/text()').extract()
        except:
            item['pc_lowest_price_per_unit'] = None
        try:
            item['pc_lowest_price'] = response.xpath('/html/body/div[2]/div/section[3]/ul/li[1]/div[1]/div[4]/a/text()').extract()
        except:
            item['pc_lowest_price'] = None
        try:
            item['pc_online_pharmacy'] = str(str(response.xpath('/html/body/div[2]/div/section[3]/ul/li[1]/div[1]/div[1]/a[1]/img').extract()).split('title="')[1]).split('"')[0]
        except:
            item['pc_online_pharmacy'] = None
        pc_not_offered = str(response.xpath('/html/body/div[2]/div/section[3]/ul/li/text()').extract())
        if 'do not offer' in pc_not_offered or 'controlled substance' in pc_not_offered:
            item['pc_not_offered'] = pc_not_offered
        else:
            item['pc_not_offered'] = None
        return item
