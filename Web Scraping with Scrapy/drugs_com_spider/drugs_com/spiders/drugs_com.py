import scrapy
from drugs_com.items import DrugsComItem

class DrugsCom(scrapy.Spider):
    name = 'drugs_com'
    allowed_domains = ['drugs.com']
    start_urls = ['https://www.drugs.com/drug_information.html']

    def parse(self, response):
        root_domain = 'https://www.drugs.com'
        a_z_pages = response.xpath('//*[@id="content"]/div[2]/div[2]/p/a/@href').extract()
        while len(a_z_pages)!=0:
            item = DrugsComItem()
            item['letter_url1'] = root_domain + a_z_pages[0].strip("[,]'")
            request = scrapy.Request(item['letter_url1'], callback = self.parseIndividualLetters)
            request.meta['DrugsComItem'] = item
            del(a_z_pages[0])
            yield request

    def parseIndividualLetters(self, response):
        root_domain = 'https://www.drugs.com'
        letter_pages = response.xpath('//*[@id="content"]/div[2]/div[3]/table/tr/td[2]/a/@href').extract()
        while len(letter_pages)!=0:
            item = DrugsComItem()
            item['letter_url2'] = root_domain + letter_pages[0].strip("[,]'")
            request = scrapy.Request(item['letter_url2'], callback = self.parseDrugs)
            request.meta['DrugsComItem'] = item
            del(letter_pages[0])
            yield request

    def parseDrugs(self, response):
        root_domain = 'https://www.drugs.com'
        drug_pages = response.xpath('//*[@id="content"]/div[2]/ul/li').extract()
        while len(drug_pages)!=0:
            item = DrugsComItem()
            drug_pages[0] = str(str(drug_pages[0]).split('href="')[1]).split('">')[0]
            item['drug_url'] = root_domain + drug_pages[0]
            request = scrapy.Request(item['drug_url'], callback = self.parseDrugData)
            request.meta['DrugsComItem'] = item
            del(drug_pages[0])
            yield request

    def parseDrugData(self, response):
        item = response.meta['DrugsComItem']
        item = self.getDrugInfo(item, response)
        return item

    def getDrugInfo(self, item, response):
        drug_name = 0
        while drug_name == 0:
            drug_name = response.xpath('//*[@id="content"]/div[2]/h1/text()').extract()
            drug_name = response.xpath('//*[@id="content"]/div[2]/div[1]/h1/text()').extract()
            drug_name = response.xpath('//*[@id="content"]/div[2]/div[2]/h1').extract()
            drug_name = 1
        item['drug_name'] = drug_name
        item['generic_name'] = response.xpath('//*[@id="content"]/div[2]/p[1]/a/text()').extract()
        brand_names = 0
        while brand_names == 0:
            brand_names = response.xpath('//*[@id="content"]/div[2]/p[1]/i/text()').extract()
            brand_names = response.xpath('//*[@id="content"]/div[2]/table/tr/td[1]/a/b/text()').extract()
            brand_names = response.xpath('//*[@id="content"]/div[2]/ul[1]/li/text()').extract()
            brand_names = 1
        item['brand_names'] = brand_names
        item['num_serious_interactions'] = len(response.xpath('//*[@id="content"]/div[2]/ul[3]/li/text()').extract())
        item['num_common_side_effects'] = len(response.xpath('//*[@id="content"]/div[2]/ul[11]/li/text()').extract())
                                                             # //*[@id="content"]/div[2]/ul[2]/li[1]/p
                                                             //*[@id="content"]/div[2]/ul[9]/li[1]
        item['pregnancy_category'] = response.xpath('//*[@id="content"]/div[2]/table/tr[2]/td[2]/text()').extract()
        return item
