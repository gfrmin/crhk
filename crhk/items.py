# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CompanyRecord(scrapy.Item):
    crno = scrapy.Field()
    companynames = scrapy.Field()
    companytype = scrapy.Field()
    dateofincorporation = scrapy.Field()
    activestatus = scrapy.Field()
    remarks = scrapy.Field()
    windingup = scrapy.Field()
    dateofdissolution = scrapy.Field()
    registerofcharges = scrapy.Field()
    note = scrapy.Field()
    namehistory = scrapy.Field()
