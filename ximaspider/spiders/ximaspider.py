# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import ssl
from scrapy.http import Request
import re
from ximaspider.items import XimaspiderItem
class TbSpider(scrapy.Spider):
    name = "ximaspider"
    allowed_domains = ["ximalaya.com"]
    start_urls = (
        'www.ximalaya.com/toutiao/',
    )
#radio_name,categary,detail,title,track_id,track_url,playnum,update_time
    def parse(self, response):
        key="shehui"
        for i in range(0,10):
            url="https://www.ximalaya.com/toutiao/"+key
            yield Request(url=url,callback=self.page)
    def page(self,response):
        #title=response.xpath("/html/head/title").extract()
        body=response.body.decode("utf-8","ignore")
        patid='"nid":"(.*?)"'
        allid=re.compile(patid).findall(body)
        print(allid)
        for j in range(0,len(allid)):
            thisid=allid[j]
            url1="https://item.taobao.com/item.htm?id="+str(thisid)
            yield Request(url=url1,callback=self.next)
    def next(self,response):
        item=XimaspiderItem()
        item["title"]=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
        item["link"]=response.url
        item["price"]=response.xpath("//input[@name='current_price']/@value").extract()
        patid='id=(.*?)$'
        thisid=re.compile(patid).findall(response.url)[0]
        commenturl="https://rate.taobao.com/detailCount.do?callback=jsonp100&itemId="+str(thisid)
        #print(commenturl)
        ssl._create_default_https_context=ssl._create_unverified_context
        commentdata=urllib.request.urlopen(commenturl).read().decode("utf-8","ignore")
        pat='"count":(.*?)}'
        item["comment"]=re.compile(pat).findall(commentdata)
        yield item