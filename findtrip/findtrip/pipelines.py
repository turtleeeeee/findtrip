# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from findtrip.spiders.washctrip import wash
import datetime
from findtrip.flight_item import Session, FlightItem
import logging

class SqlAlchemyPipeline(object):
    def __init__(self):
        # 设置日志
        self.logger = logging.getLogger(__name__)


    def open_spider(self, spider):
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        self.logger.debug('Processing item: {}'.format(item))

        if item['site'] == 'Qua':
            # 清洗数据
            item = self.wash_data(item)
            # 验证数据
            for data_key in item.keys():
                if not item[data_key]:
                    raise Exception("Missing data in {0}!".format(data_key))
        # 创建新的 FlightItem 对象并添加到数据库
        flight = FlightItem(**dict(item))
        self.session.add(flight)
        self.session.commit()
        return item

    def wash_data(self, item):
        for key in ['company', 'flight_time', 'airports', 'passtime', 'price']:
            if item.get(key):
                item[key] = wash(item[key])
        return item
'''
class QuaPipeline(object):
    def process_item(self, item, spider):
        if item['company']:
            item['company'] = wash(item['company'])
        if item['flight_time']:
            item['flight_time'] = wash(item['flight_time'])
        if item['airports']:
            item['airports'] = wash(item['airports'])
        if item['passtime']:
            item['passtime'] = wash(item['passtime'])
        if item['price']:
            item['price'] = wash(item['price'])
        return item
        '''
