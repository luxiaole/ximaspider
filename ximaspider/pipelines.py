# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class XimaspiderPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="tb")

    def process_item(self, item, spider):
        try:
            # 电台名
            radio_name = item["radio_name"][0]
            # 分类
            categary = item["categary"][0]
            # 电台介绍
            detail = item["detail"][0]
            # 音频标题
            title = item["title"][0]
            # 音频id
            track_id = item["track_id"][0]
            # 音频链接
            track_url = item["track_url"][0]
            # 播放量
            playnum = item["playnum"][0]
            # 更新时间
            update_time = item["update_time"][0]
            # title = item["title"][0]
            # link = item["link"]
            # price = item["price"][0]
            # comment = item["comment"][0]
            sql = "insert into goods(radio_name,categary,detail,title,track_id,track_url,playnum,update_time) values('" + radio_name + "','" + categary + "','" + detail + "','" + title + "','" + track_id + "','" + track_url + "','" + playnum + "','" + update_time + "')"
            self.conn.query(sql)
            # print(title)
            # print(link)
            # print(price)
            # print(comment)
            return item
        except Exception as e:
            pass

    def close_spider(self):
        self.conn.close()