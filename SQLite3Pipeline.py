# -*- coding: utf-8 -*-
import sqlite3
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class FirstspyderPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("myflights.db")
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS flights_tb""")
        self.curr.execute("""create table flights_tb(
                        price text,
                        trip text,
                        test text
                        )""")

    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self,item):
        self.curr.execute("""insert into flights_tb values (?,?,?)""",(
            item['price'][0],
            item['trip'][0],
            item['test'][0]
        ))
        self.conn.commit()