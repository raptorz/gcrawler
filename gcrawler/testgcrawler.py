# -*- coding: utf-8 -*-
"""
    test gcrawler
    ~~~~~~~~~~~~~~~~
    BSD License.
    2011-12 by raptor.zh@gmail.com.
"""
from gcrawler import Scheduler
import urllib2
from datetime import datetime
import feedparser

import logging

logging.basicConfig(level=logging.DEBUG)


urls = ['http://www.163.com', 'http://www.qq.com', 'http://www.sina.com.cn',
        'http://www.sohu.com', 'http://www.yahoo.com', 'http://www.baidu.com',
        'http://www.apple.com', 'http://www.microsoft.com']

feeds = ['http://blog.csdn.net/raptor/rss/list',
         'http://raptorz.blog.163.com/rss',
         'http://blog.sina.com.cn/rss/1494841702.xml']


def rss_fetcher(url):
    return feedparser.parse(url)


def parser(req_url, data):
    return [len(data)]


def pipeline(response):
    url = response.request.url
    print "Data fetched: %s %s" % (url, response.result[0])


import unittest


class TestGCrawler(unittest.TestCase):
    def testCrawler(self):
        dt = datetime.now()
        Scheduler(urls, parser, pipeline, max_running=8)
        print datetime.now() - dt


class TestDownloader(unittest.TestCase):
    def testDownloader(self):
        dt = datetime.now()
        Scheduler(feeds, parser, pipeline, rss_fetcher, max_running=8)
        print datetime.now() - dt


unittest.main()
