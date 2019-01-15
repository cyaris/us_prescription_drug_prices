import scrapy
from drug_bank.items import DrugBankItem
import pandas as pd
import re

class DrugBank(scrapy.Spider):
    name = 'drug_bank'
    allowed_domains = ['drugbank.ca']
    start_urls = [
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=1&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=2&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=3&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=4&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=5&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=6&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=7&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=8&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=9&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=10&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=11&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=12&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=13&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=14&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=15&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=16&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=17&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=18&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=19&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=20&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=21&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=22&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=23&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=24&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=25&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=26&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=27&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=28&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=29&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=30&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=31&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=32&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=33&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=34&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=35&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=36&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=37&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=38&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=39&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=40&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=41&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=42&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=43&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=44&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=45&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=46&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=47&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=48&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=49&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=50&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=51&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=52&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=53&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=54&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=55&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=56&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=57&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=58&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=59&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=60&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=61&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=62&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=63&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=64&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=65&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=66&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=67&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=68&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=69&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=70&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=71&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=72&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=73&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=74&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=75&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=76&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=77&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=78&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=79&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=80&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=81&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=82&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=83&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=84&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=85&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=86&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=87&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=88&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=89&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=90&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=91&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=92&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=93&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=94&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=95&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=96&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=97&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=98&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=99&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=100&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=101&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=102&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=103&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=104&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=105&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=106&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=107&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=108&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=109&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=110&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=111&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=112&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=113&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=114&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=115&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=116&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=117&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=118&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=119&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=120&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=121&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=122&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=123&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=124&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=125&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=126&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=127&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=128&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=129&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=130&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=131&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=132&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=133&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=134&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=135&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=136&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=137&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=138&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=139&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=140&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=141&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=142&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=143&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=144&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=145&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=146&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=147&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=148&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=149&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=150&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=151&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=152&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=153&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=154&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=155&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=156&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=157&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=158&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=159&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=160&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=161&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=162&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=163&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=164&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=165&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=166&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=167&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=168&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=169&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=170&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=171&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=172&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=173&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=174&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=175&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=176&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=177&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=178&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=179&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=180&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=181&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=182&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=183&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=184&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=185&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=186&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=187&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=188&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=189&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=190&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=191&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=192&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=193&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=194&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=195&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=196&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=197&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=198&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=199&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=200&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=201&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=202&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=203&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=204&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=205&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=206&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=207&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=208&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=209&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=210&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=211&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=212&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=213&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=214&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=215&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=216&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=217&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=218&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=219&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=220&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=221&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=222&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=223&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=224&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=225&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=226&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=227&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=228&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=229&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=230&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=231&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=232&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=233&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=234&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=235&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=236&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=237&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=238&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=239&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=240&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=241&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=242&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=243&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=244&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=245&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=246&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=247&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=248&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=249&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=250&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=251&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=252&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=253&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=254&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=255&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=256&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=257&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=258&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=259&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=260&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=261&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=262&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=263&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=264&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=265&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=266&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=267&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=268&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=269&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=270&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=271&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=272&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=273&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=274&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=275&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=276&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=277&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=278&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=279&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=280&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=281&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=282&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=283&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=284&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=285&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=286&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=287&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=288&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=289&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=290&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=291&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=292&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=293&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=294&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=295&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=296&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=297&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=298&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=299&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=300&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=301&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=302&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=303&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=304&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=305&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=306&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=307&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=308&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=309&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=310&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=311&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=312&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=313&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=314&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=315&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=316&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=317&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=318&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=319&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=320&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=321&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=322&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=323&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=324&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=325&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=326&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=327&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=328&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=329&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=330&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=331&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=332&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=333&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=334&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=335&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=336&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=337&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=338&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=339&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=340&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=341&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=342&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=343&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=344&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=345&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=346&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=347&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=348&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=349&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=350&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=351&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=352&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=353&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=354&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=355&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=356&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=357&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=358&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=359&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=360&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=361&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=362&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=363&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=364&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=365&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=366&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=367&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=368&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=369&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=370&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=371&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=372&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=373&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=374&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=375&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=376&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=377&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=378&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=379&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=380&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=381&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=382&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=383&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=384&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=385&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=386&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=387&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=388&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=389&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=390&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=391&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=392&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=393&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=394&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=395&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=396&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=397&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=398&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=399&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=400&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=401&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=402&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=403&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=404&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=405&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=406&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=407&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=408&us=0&withdrawn=0',
    'https://www.drugbank.ca/drugs?approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=409&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=1&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=2&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=3&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=4&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=5&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=6&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=7&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=8&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=9&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=10&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=11&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=12&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=13&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=14&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=15&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=16&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=17&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=18&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=19&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=20&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=21&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=22&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=23&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=24&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=25&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=26&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=27&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=28&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=29&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=30&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=31&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=32&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=33&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=34&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=35&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=36&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=37&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=38&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=39&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=40&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=41&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=42&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=43&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=44&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=45&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=46&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=47&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=48&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=49&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=50&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=51&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=52&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=53&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=54&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=55&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=56&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=57&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=58&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=59&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=60&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=61&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=62&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=63&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=64&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=65&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=66&us=0&withdrawn=0',
    'https://www.drugbank.ca/biotech_drugs?Allergenics=0&Cell+transplant+therapies=0&Gene+Therapies=0&Nucleic+Acid+Based+Therapies=0&Protein+Based+Therapies=0&Vaccines=0&approved=0&c=name&canada=0&d=up&eu=0&experimental=0&illicit=0&investigational=0&nutraceutical=0&page=67&us=0&withdrawn=0'
    ]

    def parse(self, response):
        root_domain = 'https://www.drugbank.ca'
        pages = response.xpath('//*[@id="drugs-table"]/tbody/tr/td[1]/strong/a/@href').extract()
        while len(pages)!=0:
            item = DrugBankItem()
            item['page_url'] = root_domain + pages[0]
            request = scrapy.Request(item['page_url'], callback = self.parseDrugBankData)
            request.meta['DrugBankItem'] = item
            del(pages[0])
            yield request

    def parseDrugBankData(self, response):
        item = response.meta['DrugBankItem']
        item = self.getDrugBankInfo(item, response)
        return item

    def getDrugBankInfo(self, item, response):
        root_domain = 'https://www.drugbank.ca'
        try:
            item['db_drug_name'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[1]/text()').extract()
        except:
            item['db_drug_name'] = None
        try:
            item['db_acc_num'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[2]/text()').extract()
        except:
            item['db_acc_num'] = None
        try:
            item['db_drug_type'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[3]/text()').extract()
        except:
            item['db_drug_type'] = None
        try:
            item['db_drug_group'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[4]/text()').extract()
        except:
            item['db_drug_group'] = None
        # item['db_drug_description'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[5]/text()').extract()
        # item['db_drug_category'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[9]/div/span/text()').extract()
        try:
            item['db_cas_num'] = str(str(response.xpath('/html').extract()).split('CAS number</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_cas_num'] = None
        # item['db_cas_num'] = str(str(response.xpath('//dd')[13].extract()).split('">')[1]).split('</')[0]
        # item['db_cas_num'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[11]/text()').extract()
        try:
            item['db_molecular_weight'] = str(str(response.xpath('/html').extract()).split('Weight</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_molecular_weight'] = None
        # item['db_molecular_weight'] = str(str(response.xpath('//dd')[14].extract()).split('8">')[1]).split('</dd>')[0]
        # item['db_drug_weight'] = response.xpath('/html/body/main/div/div[4]/dl[1]/dd[12]/text()').extract()
        # item['db_metabolism'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[8]/p/text()').extract()
        try:
            item['db_absorbtion'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[5]/p/text()').extract()
        except:
            item['db_absorbtion'] = None
        # item['db_vol_distribution'] = str(str(response.xpath('/html').extract()).split('Volume of distribution</dt><dd class="col-md-10 col-sm-8">')[1]).split('</span>')[0]
        # item['db_vol_distribution'] = str(str(response.xpath('//dd')[26].extract()).split('><p>')[1]).split('</p>')[0]
        # item['db_vol_distribution'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[6]/ul/li/text()').extract()#
        try:
            item['db_protein_binding'] = str(str(response.xpath('/html').extract()).split('Protein binding</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_protein_binding'] = None
        # item['db_protein_binding'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[7]/p/text()').extract()
        # item['db_clearance'] = str(str(response.xpath('/html').extract()).split('Clearance</dt><dd class="col-md-10 col-sm-8">')[1]).split('</span>')[0]
        # item['db_clearance'] = str(str(response.xpath('//dd')[31].extract()).split('"><p>')[1]).split('</p>')[0]
        # item['db_clearance'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[11]/ul/li/text()').extract()
        try:
            item['db_affected_organisms'] = str(str(response.xpath('/html').extract()).split('Affected organisms</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_affected_organisms'] = None
        # item['db_affected_organisms'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[13]/ul/li/text()').extract()
        # item['db_affected_organisms'] = str(str(response.xpath('/html').extract()).split('Affected organisms</dt><dd class="col-md-10 col-sm-8"><ul class="list-unstyled table-list"><li>')[1]).split('</li></ul>')[0]
        # item['db_affected_organisms'] = str(str(response.xpath('//dd')[31].extract()).split('><li>')[1]).split('</li>')[0]
        # item['db_adrs'] = response.xpath('/html/body/main/div/div[4]/dl[2]/dd[15]/span/text()').extract()
        try:
            item['db_synth_ref'] = response.xpath('/html/body/main/div/div[4]/dl[4]/dd[1]/span/p/text()').extract()
        except:
            item['db_synth_ref'] = None
        try:
            item['db_num_manufacturers'] = len(response.xpath('/html/body/main/div/div[4]/dl[6]/dd[1]/div/ul/li/text()').extract())
        except:
            item['db_num_manufacturers'] = None
        try:
            item['db_num_packagers'] = len(response.xpath('/html/body/main/div/div[4]/dl[6]/dd[2]/div/ul/li/text()').extract())
        except:
            item['db_num_packagers'] = None
        try:
            item['db_num_dosage_forms'] = len(response.xpath('//*[@id="dosages"]/tbody/tr').extract())
        except:
            item['db_num_dosage_forms'] = None
        try:
            item['db_num_patents'] = len(response.xpath('//*[@id="patents"]/tbody/tr/td[1]/a/text()').extract())
        except:
            item['db_num_patents'] = None
        # item['db_melting_point'] = response.xpath('//*[@id="experimental-properties"]/tbody/tr[1]/td[2]/text()').extract()
        # item['db_water_solubility'] = response.xpath('//*[@id="experimental-properties"]/tbody/tr[2]/td[2]/text()').extract()
        # item['db_log_p'] = response.xpath('//*[@id="experimental-properties"]/tbody/tr[3]/td[2]/text()').extract()
        try:
            item['db_chem_state'] = response.xpath('/html/body/main/div/div[4]/dl[7]/dd[1]/text()').extract()
        except:
            item['db_chem_state'] = None
        try:
            item['db_kingdom'] = response.xpath('/html/body/main/div/div[4]/dl[9]/dd[2]/a/text()').extract()
        except:
            item['db_kingdom'] = None
        try:
            item['db_super_class'] = str(str(response.xpath('/html').extract()).split('Super Class</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_super_class'] = None
        try:
            item['db_class'] = str(str(response.xpath('/html').extract()).split('>Class</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_class'] = None
        try:
            item['db_sub_class'] = str(str(response.xpath('/html').extract()).split('Sub Class</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_sub_class'] = None
        try:
            item['db_molecular_framework'] = str(str(response.xpath('/html').extract()).split('Molecular Framework</dt><dd class="col-md-10 col-sm-8">')[1]).split('</dd>')[0]
        except:
            item['db_molecular_framework'] = None
        try:
            item['db_num_food_interactions'] = len(response.xpath('/html/body/main/div/div[4]/dl[3]/dd[2]/ul/li/text()').extract())
        except:
            item['db_num_food_interactions'] = None
        # item['db_ahfs_code'] = response.xpath('/html/body/main/div/div[4]/dl[4]/dd[5]/ul/li/text()').extract()
        try:
            item['db_brand_names_table_url'] = root_domain + '/drugs' + str(response.url).split('drugs')[1] + '/products.json?group=approved'
        except:
            item['db_brand_names_table_url'] = None
        df = pd.read_json(item['db_brand_names_table_url'])
        try:
            item['db_brand_names'] = set(([s.split(',')[0] for s in df['data'].astype(str)]))
        except:
            item['db_brand_names'] = None
        try:
            item['db_generic_names_table_url'] = root_domain + '/drugs' + str(response.url).split('drugs')[1] + '/products.json?group=generic'
        except:
            item['db_generic_names_table_url'] = None
        df = pd.read_json(item['db_generic_names_table_url'])
        try:
            item['db_generic_names'] = set(([s.split(',')[0] for s in df['data'].astype(str)]))
        except:
            item['db_generic_names'] = None
        try:
            item['db_mixture_products_table_url'] = root_domain + '/drugs' + str(response.url).split('drugs')[1] + '/products.json?group=mixtures'
        except:
            item['db_mixture_products_table_url'] = None
        df = pd.read_json(item['db_mixture_products_table_url'])
        try:
            item['db_mixture_names'] = set(([s.split(',')[0] for s in df['data'].astype(str)]))
        except:
            item['db_mixture_names'] = None
        try:
            item['db_drug_interactions_url'] = root_domain + '/drugs' + str(response.url).split('drugs')[1] + '/drug_interactions.json'
        except:
            item['db_drug_interactions_url'] = None
        df = pd.read_json(item['db_drug_interactions_url'])
        try:
            item['db_num_drug_interactions'] = len(df['recordsTotal'])
        except:
            item['db_num_drug_interactions'] = None
        try:
            item['db_num_clin_trials'] = len(re.findall('(?=/clinical_trials?)', str(response.xpath('//dl')[5].extract())))
        except:
            item['db_num_clin_trials'] = None
        try:
            item['db_num_targets'] = len(re.findall('(?=href="#)', response.xpath('//table/tbody')[4].extract()))
        except:
            item['db_num_targets'] = None
        return item

    # def load_common_fields(item_loader, response):
    #     '''Load field values which are common to "on sale" and "recently sold" properties.'''
    #     item_loader.add_value('url', response.url)
    #     item_loader.add_xpath('address', '//*[@data-role="address"]/text()')
    #     item_loader.add_xpath('city_state', '//*[@data-role="cityState"]/text()')
    #     item_loader.add_xpath('price', '//span[@data-role="price"]/text()', re=r'\$([\d,]+)')
    #     item_loader.add_xpath('neighborhood', '//*[@data-role="cityState"]/parent::h1/following-sibling::span/a/text()')
    #     details = item_loader.nested_css('.homeDetailsHeading')
    #     overview = details.nested_xpath('.//span[contains(text(), "Overview")]/parent::div/following-sibling::div[1]')
    #     overview.add_xpath('overview', xpath='.//li/text()')


        # response.xpath('/html/body/main/div/div[4]')
        # str(str(str(str(response.xpath('//dd').extract()).split(',')).split('</thead><tbody><tr><td><strong>')[2:5]).split('</strong></td><td>')).split('<tr><td><strong>')
        # str(str(str(response.xpath('//dd').extract()).split('</thead><tbody><tr><td><strong>').split('</strong></td><td>').split('<tr><td><strong>')

        # for i, item in enumerate(response.xpath('//dd')):
        #     print(i, item)
        #
        # for i, item in enumerate(response.xpath('//*[@class]')):
        #     print(i, item)

        # response.xpath('/html/body/main/div').extract()
        # response.xpath('//*[@class="dataTables_wrapper dt-bootstrap4 no-footer"]')
        # response.xpath('//*[@class="carousel-control-next-icon"]').extract()
        # response.xpath('//*[@class="drug-image"]/text()').extract()
        # response.xpath('//*[@class="separated-list-item"]/text()').extract()
        # response.xpath('//*[@class="separated-list-item"]')
        # response.xpath('//*[@class="list-separator"]')
        # response.xpath('//*[@class="col-sm-12"]')
        # response.xpath('//*[@class="col-md-10 col-sm-8"]')[10:14].extract()
        # response.xpath('//*[@class="carousel-control-next"]')
        # response.xpath('//*[@class="sr-only"]')
        # response.xpath('//*[@class="table table-sm datatable"]')
        # response.xpath('//*[@class="col-md-10 col-sm-8"]')
        # response.xpath('//*[@class="col-md-2 col-sm-4"]')
        # dd class="col-md-10 col-sm-8
        # response.xpath('//*[@class="products table table-sm dt"]')
        # response.xpath('//*[@class="products table table-sm dt-responsive datatable-remote"]')
        # response.xpath('//*[@class="products table table-sm dt-responsive datatable-remote"]/tbody/tr/td/strong/text()').extract()
        # response.xpath('//*[@class="col-md-10 col-sm-8"]/table/tbody')[9].extract()
        # response.xpath('//*[@class="col-md-10 col-sm-8"]/table/tbody/tr/td[1]').extract()






        # str(response.xpath('//*[@class]')[227].extract()).split('<tr><td><strong>')[1:]
        # str(response.xpath('/html/body/main/div').extract()).split('" style="width: 100%"><thead><th>Name</th><th>Dosage</th><th>Strength</th><th>Route</th><th>Labeller</th><th>Marketing Start</th><th>Marketing End</th><th></th><th class="drug-image"></th></thead><tbody><tr><td><strong>')
        # str(str(str(str(str(str(str(str(str(response.xpath('/html/body/main/div').extract()).split(',')).split('>')).split('<')).replace(']', '')).replace('[', '')).replace('"', '')).replace(",", '')).replace("\\", '')).split('/')
