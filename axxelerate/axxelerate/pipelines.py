# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import credentials


class AxxeleratePipeline(object):
    connection = pymysql.connect(host = credentials.host,
    						user = credentials.user,
    						password = credentials.password,
    						cursorclass = pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
    	try:
    		with self.connection.cursor() as cursor:
    			sql = "INSERT INTO `urlinfo` (`url`) VALUES (%s)"
    			cursor.execute(sql, (item['url']))
    		self.connection.commit()
    	except: 
    		pass
    	return item
