#!/usr/bin/env python
# coding=utf-8

import url_manger,html_downloader,html_parse,html_outputer

class SpiderMain(object):
    def __init(self):
        self.urls = url_manger.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self,root_url):
        cout = 1
        slef.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                new_url = slef.urls.get_newurl()
                print 'craw %d:%s'%(count,new_url)
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            
                print "hello python"
                if count == 1000:
                    break
        except:
            print "craw failed"
        self.outputer.output_html()

if __name__ == "main":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

root_url = "http://blog.fanfou.com/digest/#2018-02-10.daily"
html_cont = html_downloader.HtmlDownloader().download(root_url);
print html_cont
