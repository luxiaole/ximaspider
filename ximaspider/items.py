# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XimaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电台名
    radio_name = scrapy.Field()
    #分类
    categary = scrapy.Field()
    # 电台介绍
    detail = scrapy.Field()
    # 音频标题
    title = scrapy.Field()
    #音频id
    track_id = scrapy.Field()
    #音频链接
    track_url = scrapy.Field()
    #播放量
    playnum = scrapy.Field()
    #更新时间
    update_time = scrapy.Field()