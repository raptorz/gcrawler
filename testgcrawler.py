# -*- coding: utf-8 -*-
"""
    test gcrawler
    ~~~~~~~~~~~~~~~~
    BSD License.
    2011-12 by raptor.zh@gmail.com.
"""
from gcrawler import Scheduler
import unittest
import urllib2
import logging
import traceback
from datetime import datetime
import re

logging.basicConfig(level=logging.DEBUG)

urls = ['http://www.163.com', 'http://www.qq.com', 'http://www.sina.com.cn',
        'http://www.sohu.com', 'http://www.yahoo.com', 'http://www.baidu.com',
        'http://www.apple.com', 'http://www.microsoft.com']

feeds = ['http://feeds.feedburner.com/raptor_we8log',
         'http://feeds.feedburner.com/we8log_photo']


class Crawler:
    def fetcher(self, url):
        import feedparser
        return feedparser.parse(url)

    def parser(self, req_url, data):
        return [len(data)]

    def pipeline(self, response):
        url = response.request.url
        print "Data fetched: %s %s" % (url, response.result[0])


class TestGCrawler(unittest.TestCase):
    def testCrawler(self):
        dt = datetime.now()
        crawler = Crawler()
        Scheduler(urls, crawler.parser, crawler.pipeline, max_running=8)
        print datetime.now() - dt


class TestDownloader(unittest.TestCase):
    def testDownloader(self):
        dt = datetime.now()
        crawler = Crawler()
        Scheduler(feeds, crawler.parser, crawler.pipeline, crawler.fetcher, max_running=8)
        print datetime.now() - dt

unittest.main()
