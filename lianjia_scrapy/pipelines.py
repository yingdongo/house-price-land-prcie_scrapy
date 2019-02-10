# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymysql

class MySQLLandPipeline(object):
    
    # 打开数据库
    def open_spider(self, spider):
        self.db_conn =pymysql.connect(host='xxx.xx.xx.xx', port=3306, db='test', user='root', passwd='xxxxxx', charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
           item['title'],
           item['trade_time'],
           item['buyer'],
           item['commercial_ratio'],
           item['construction_land_area'],
           item['district_id'],
           item['floor_area'],
           item['land_id'],
           item['location'],
           item['plot_ratio'],
           item['starting_price'],
           item['total_land_area'],
           item['total_price'],
           item['trade_form'],
           item['trade_result'],
           item['unit_price'],
           item['land_usage'],
           item['writeTime'],
       )


        sql = 'INSERT INTO cd_land VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)
class MySQLCommunityPipeline(object):

    # 打开数据库
    def open_spider(self, spider):
        self.db_conn =pymysql.connect(host='xxx.xx.xx.xx', port=3306, db='test', user='root', passwd='xxxxxx', charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    #插入数据
    def insert_db(self, item):
        values = (
            item['community_id'],
            item['community_name'],
            item['community_average_price'],
            item['building_age'],
            item['district'],
            item['district_id'],
            item['level'],
            item['year'],
            item['month'],
            item['writeTime'],
        )

        sql = 'INSERT INTO cd_community VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)

class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    # words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):

        if item['community_average_price']:
            return item
        else:
            logging.debug(item['community_average_price'])
            
