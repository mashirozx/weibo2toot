#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on May 29, 2020
Desc: Media file downloader
Author: Mashiro
URL: https://2heng.xin
License: MIT
"""
from .get_config import GetConfig

config = GetConfig()

def MediaDownloader(data):
  """
  :param object: Data return from TweetDecoder
  :return {'gif_count': (max+1)gif_id, 'video_count': video_id, 'image_count': img_id, 'plain': str}
  """
  res = {'video_count': None, 'image_count': None, 'plain': None, 'video_link': None}
  att = ''

  if data['image']:
    att = att + '\n'
    for url in data['image']:
      att = att + 'IMAGE: [' + url + ']\n'

  if data['video']:
    att = att + '\n'
    att = att + 'VIDEO: ['+data['video'][0] +'] {'+data['video_poster'][0] +'}\n'

    res['video_link'] = data['video'][0]

  res['plain']=data['plain'] + att

  return res

if __name__ == '__main__':
  test_data = {'gif': ['https://video.twimg.com/tweet_video/EZLxKmTUMAARbSa.mp4'], 'gif_poster': ['https://pbs.twimg.com/tweet_video_thumb/EZLxKmTUMAARbSa.jpg'], 'video': ['https://video.twimg.com/ext_tw_video/1265470079203827712/pu/vid/1280x720/B-BRCBM0djUAqJl0.mp4?tag=10'], 'video_poster': ['https://pbs.twimg.com/ext_tw_video_thumb/1265470079203827712/pu/img/VujsmqbQORfHDeCP.jpg'], 'image': ['https://pbs.twimg.com/media/EZJh5RPUMAEz4aS?format=jpg&name=orig','https://s3-view.2heng.xin/aws_cached/2019/07/14/53c2adbc381e3aa17968d5d36feee002.md.png', 'https://s3-view.2heng.xin/aws_cached/2020/05/19/b1a7d8ff391616ad152f9958c6302ba0.md.jpg', 'https://s3-view.2heng.xin/aws_cached/2020/05/18/671a82563dfe40885196166683bf6f0b.md.jpg'], 'plain': '流程图工具 Excalidraw 可以做出下面这样的图示效果，可惜中文没有手写效果。 https://excalidraw.com/ '}
  MediaDownloader(test_data)
