# coding=utf-8

import scrapy

from crhk.items import CompanyRecord

class CrhkSpider(scrapy.Spider):
    name = "crhk"
    allowed_domains = ["mobile-cr.gov.hk"]
    start_urls = ["https://www.mobile-cr.gov.hk/mob/cps_criteria.do?queryCRNO=0100001"]

    def parse(self, response):
        namestds = response.css("td.data::text").extract()   # historical dates of different names
    
        item = CompanyRecord()
        item['crno'] = response.css(".info tr:nth-child(1) td:nth-child(2)::text").extract()
        item['companynames'] = response.css("tr:nth-child(2) td::text").extract()
        item['companytype'] = response.css("tr:nth-child(3) td::text").extract()
        item['dateofincorporation'] = response.css("tr:nth-child(4) td::text").extract()
        item['activestatus'] = response.css("tr:nth-child(5) td::text").extract()
        item['remarks'] = response.css(".sameasbody::text").extract()
        item['windingup'] = response.css("tr:nth-child(7) td::text").extract()
        item['dateofdissolution'] = response.css("tr:nth-child(8) td::text").extract()
        item['registerofcharges'] = response.css("tr:nth-child(9) td::text").extract()
        item['note'] = response.css("tr:nth-child(10) td::text").extract()
        item['namehistory'] = response.css("td.data::text").extract()
        yield(item)
    
