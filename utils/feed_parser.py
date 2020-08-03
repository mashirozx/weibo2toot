#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on May 29, 2020
Desc: RSS feed parser
Author: Mashiro 
URL: https://2heng.xin
License: MIT
"""
import feedparser

def FeedParaser(rss_link):
  """
  :param str: RSS URL
  :return object: rss object
  """
  RssHubFeed = feedparser.parse(rss_link)

  rss = []

  for item in RssHubFeed.entries:
    data={}
    # for detail in item.keys():
    #   data[detail]=item[detail]
    data['title']=item['title']
    data['summary']=item['summary']
    data['id']=item['id']
    data['link']=item['link']
    rss.append(data)
    
  # print(rss)
  return rss
  
if __name__ == '__main__':
  print(str(FeedParaser("https://rsshub.app/bilibili/user/dynamic/161775300")))