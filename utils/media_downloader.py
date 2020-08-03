#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on May 29, 2020
Desc: Media file downloader
Author: Mashiro 
URL: https://2heng.xin
License: MIT
"""
import urllib.request
# import ffmpy
from .get_config import GetConfig

config = GetConfig()

def MediaDownloader(data):
  """
  :param object: Data return from TweetDecoder
  :return {'gif_count': (max+1)gif_id, 'video_count': video_id, 'image_count': img_id, 'plain': str}
  """
  # set header
  opener = urllib.request.build_opener()
  opener.addheaders = []
  opener.addheaders.append(('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'))
  opener.addheaders.append(('Referer', 'https://weibo.com/'))
  urllib.request.install_opener(opener)

  res = {'video_count': None, 'image_count': None, 'plain': None, 'video_link': None}

  if data['image']:
    img_id = 1
    for url in data['image']:
      if (img_id <= 4):
        try:
          urllib.request.urlretrieve(url, 'temp/img'+str(img_id)+'.png')
          img_id = img_id+1
        except Exception:
          print(f'ERRO: failed[img]: {url}')
          # for e in Exception:
          #   print(e)

    res['image_count']=img_id

  if data['video']:
    video_id = 1
    for url in data['video']:
      if (video_id <= 1):
        try:
          if config['MASTODON']['IncludeVideo'] != 'false':
            urllib.request.urlretrieve(url, 'temp/video'+str(video_id)+'.mp4')

          urllib.request.urlretrieve(data['video_poster'][video_id-1], 'temp/video'+str(video_id)+'.png')
          res['video_link']=url
          video_id = video_id+1
        except Exception:
          print(f'ERRO: failed[vid]: {url}')
          # for e in Exception:
          #   print(e)

    res['video_count']=video_id
  
  res['plain']=data['plain']

  return res

if __name__ == '__main__':
  test_data = {'gif': ['https://video.twimg.com/tweet_video/EZLxKmTUMAARbSa.mp4'], 'gif_poster': ['https://pbs.twimg.com/tweet_video_thumb/EZLxKmTUMAARbSa.jpg'], 'video': ['https://video.twimg.com/ext_tw_video/1265470079203827712/pu/vid/1280x720/B-BRCBM0djUAqJl0.mp4?tag=10'], 'video_poster': ['https://pbs.twimg.com/ext_tw_video_thumb/1265470079203827712/pu/img/VujsmqbQORfHDeCP.jpg'], 'image': ['https://pbs.twimg.com/media/EZJh5RPUMAEz4aS?format=jpg&name=orig','https://s3-view.2heng.xin/aws_cached/2019/07/14/53c2adbc381e3aa17968d5d36feee002.md.png', 'https://s3-view.2heng.xin/aws_cached/2020/05/19/b1a7d8ff391616ad152f9958c6302ba0.md.jpg', 'https://s3-view.2heng.xin/aws_cached/2020/05/18/671a82563dfe40885196166683bf6f0b.md.jpg'], 'plain': '流程图工具 Excalidraw 可以做出下面这样的图示效果，可惜中文没有手写效果。 https://excalidraw.com/ '}
  MediaDownloader(test_data)