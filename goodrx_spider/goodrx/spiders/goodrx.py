import scrapy
from goodrx.items import GoodrxItem

class Goodrx(scrapy.Spider):
    name = 'goodrx'
    allowed_domains = ['goodrx.com']
    start_urls = ['https://www.goodrx.com/sitemap-drugs-1.xml',
    'https://www.goodrx.com/sitemap-drugs-2.xml']

    def parse(self, response):
        url_string = str(response.xpath('/html/body').extract()).split('\\n    ')
        url_links = []
        for string in url_string:
            if string[0:5] == '<loc>' and string[-6:] == '</loc>':
                url_links.append(string[5:-6])
        drug_urls = []
        for i, url in enumerate(url_links):
            if 'what-is' not in url_links[i] and 'latest-news' not in url_links[i] and 'side-effects' not in url_links[i] and 'savings-tips' not in url_links[i] and 'images' not in url_links[i] and 'medicare-coverage' not in url_links[i]:
                drug_urls.append(url_links[i])
        while len(drug_urls)!=0:
            item = GoodrxItem()
            item['drug_url'] = 'https://m' + drug_urls[0][11:]
            request = scrapy.Request(item['drug_url'], callback = self.parseDrugData)
            request.meta['GoodrxItem'] = item
            del(drug_urls[0])
            yield request

    def parseDrugData(self, response):
        item = response.meta['GoodrxItem']
        item = self.getDrugInfo(item, response)
        return item

    def getDrugInfo(self, item, response):
        try:
            item['grx_drug_warning'] = response.xpath('//*[@id="uat-notice-btn"]/span/text()').extract()
        except:
            item['grx_drug_warning'] = None
        try:
            item['drug_notice'] = response.xpath('//*[@id="uat-notice-text"]/text()').extract()
        except:
            item['drug_notice'] = None
        drug_name = response.xpath('//*[@id="uat-drug-title"]/text()').extract()
        if len(drug_name) == 0:
            item['drug_name'] = response.xpath('//*[@id="uat-drug-title"]/a[1]/text()').extract()
        elif set(drug_name) == {', '}:
            item['drug_name'] = response.xpath('//*[@id="uat-drug-title"]/a[1]/text()').extract()
        else:
            item['drug_name'] = drug_name
        try:
            item['generic_name'] = response.xpath('//*[@id="uat-drug-secondary-title"]/a/text()').extract()
        except:
            item['generic_name'] = None
        if len(item['generic_name']) == 0:
            try:
                item['generic_name'] = response.xpath('//*[@id="uat-drug-secondary-title"]/span/text()').extract()
            except:
                item['generic_name'] = None
        grx_lowest_price = response.xpath('//*[@id="uat-price-row-0"]/a[2]/b/text()').extract()
        if len(grx_lowest_price) == 0:
            item['grx_lowest_price'] = response.xpath('//*[@id="uat-price-row-0"]/button/b/text()').extract()
        else:
            item['grx_lowest_price'] = grx_lowest_price
        goodrx_pharmacy = response.xpath('//*[@id="uat-price-row-0"]/a[1]/div[1]/text()').extract()
        if len(goodrx_pharmacy) == 0:
            item['grx_pharmacy'] = response.xpath('//*[@id="uat-price-row-0"]/a/div[1]/text()').extract()
        else:
            item['grx_pharmacy'] = goodrx_pharmacy
        try:
            item['grx_purchase'] = response.xpath('//*[@id="uat-drug-config"]/text()').extract()[1]
        except:
            item['grx_purchase'] = None
        try:
            item['grx_avg_cash_price'] = response.xpath('//*[@id="uat-drug-price-history"]/div/span[2]/text()').extract()[0]
        except:
            item['grx_avg_cash_price'] = None
        try:
            item['grx_fair_price'] = response.xpath('//*[@id="uat-drug-price-history"]/div/span[2]/text()').extract()[1]
        except:
            item['grx_fair_price'] = None
        try:
            item['grx_over_counter'] = response.xpath('//*[@id="uat-otc-price-list"]/span[1]/text()').extract()
        except:
            item['grx_over_counter'] = None
        try:
            item['grx_popularity_rank'] = response.xpath('//*[@id="uat-price-history-popularity-rank"]/span/text()').extract()
        except:
            item['grx_popularity_rank'] = None
        try:
            item['grx_competition_amount'] = response.xpath('//*[@id="uat-price-history-popularity-rank"]/text()').extract()
        except:
            item['grx_competition_amount'] = None
        try:
            item['grx_affordability_rank'] = response.xpath('//*[@id="uat-price-history-expense-rank"]/span/text()').extract()
        except:
            item['grx_affordability_rank'] = None
        try:
            item['grx_no_prices_found'] = response.xpath('//*[@id="uat-no-prices"]/span[1]/text()').extract()
        except:
            item['gdrx_no_prices_found'] = None
        try:
            item['grx_not_avail'] = response.xpath('//*[@id="uat-price-row-container"]/div/span[1]/text()').extract()
        except:
            item['grx_not_avail'] = None
        return item
