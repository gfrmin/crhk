import logging
from time import sleep

import scrapy

class retry(object):
    def process_response(self, request, response, spider):
        if response.css("tr:nth-child(3) td::text").extract()[0] == u'\r\n\t\t\t\t\t\u5982\u8981\u7e7c\u7e8c\u67e5\u95b1\u516c\u53f8\u8cc7\u6599\uff0c\u8acb\u8f38\u5165\u4e0a\u5716\u7684\u9a57\u8b49\u5bc6\u78bc\uff1a \r\n\t\t\t\t\t':
            logging.info("Retrying %(request)s", {'request': request.url})
            return request.copy()
        else:
            return response
