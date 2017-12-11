# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import credentials

connection = pymysql.connect(host = credentials.host,
                                 user = credentials.user,
                                 password = credentials.password,
                                 db = credentials.db,
                                 cursorclass = pymysql.cursors.DictCursor)


class AxxeleratePipeline(object):
    def process_item(self, item, spider):
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO `pages` (`url`) VALUES (%s)"
                cursor.execute(sql, (item['url']))
            connection.commit()
        except:
            pass
        return item
