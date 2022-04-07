#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on May 29, 2020
Desc: Twitter HTML parser
Author: Mashiro 
URL: https://2heng.xin
License: MIT
"""
from bs4 import BeautifulSoup
from html import unescape
import re
from .get_config import GetConfig

config = GetConfig()

def TweetDecoder(rss_data):
  """
  :params object: Summary from FeedParaser
  :return object
  """
  soup = BeautifulSoup(rss_data['summary'], features='html.parser')

  data = {
      'video': [],
      'video_poster': [],
      'image': [],
      'plain': None
  }

  for link in soup.find_all('a'):
    # link.replace_with(' ' + link.get('href') + ' ')
    if (link.has_attr('data-url')):
      if ('://t.cn/' in link.get('data-url')):
        if ('微博视频' in link.getText()):
          link.replace_with(f'''[?bs4_replace_flag?] {config['MASTODON']['VideoSourcePrefix']} {link.getText()} {link.get('data-url')} [?bs4_replace_flag?]''')
        else:
          link.replace_with(f'''[?bs4_replace_flag?] {config['MASTODON']['ExternalLinkPrefix']} {link.getText()} {link.get('data-url')} [?bs4_replace_flag?]''')
      else:
        link.replace_with(f'''[?bs4_replace_flag?] {config['MASTODON']['ExternalLinkPrefix']} {link.getText()} {link.get('href')} [?bs4_replace_flag?]''')
    elif (link.getText()[-1] == '#'):
      link.replace_with(f'''[?bs4_replace_flag?] {link.getText()[:-1]} [?bs4_replace_flag?]''')
    else:
      link.replace_with('[?bs4_replace_flag?]'+link.getText()+'[?bs4_replace_flag?]')

  for span in soup.find_all('span'):
    if('url-icon' in span.get('class')):
      # print(span)
      img = span.find('img')
      img.replace_with(img.get('alt'))

  for video in soup.find_all('video'):
    # print(video.get('src'))
    if ('://f.video.weibocdn.com' in video.get('src')):
      # need to add a reffer i guess.
      data['video'].append(video.get('src'))
      data['video_poster'].append(video.get('poster'))
      video.replace_with('')

  for image in soup.find_all('img'):
    # print(video.get('src'))
    data['image'].append(image.get('src'))
    image.replace_with('')

  for br in soup.find_all('br'):
    br.replace_with('<|n>')

  for span in soup.find_all('span'):
    span.replace_with('')
    # span.replace_with(span.text)

  for div in soup.find_all('div'):
    div.replace_with('')

  for blockquote in soup.find_all('blockquote'):
    blockquote.unwrap()
  
  # print(soup.prettify())
  # print(str(data))
  plain_content = unescape(soup.prettify())
  plain_content = plain_content.replace('  ', ' ')
  plain_content = plain_content.replace('\n[?bs4_replace_flag?]',' ').replace('[?bs4_replace_flag?]\n',' ').replace('[?bs4_replace_flag?]','').replace('\n- ','\n\- ').replace('<|n>','\n')
  # plain_content = re.sub(r'(#[^#]+)#', lambda m : m.group(1)+' ', plain_content)
  data['plain'] = plain_content + '\n'+config['MASTODON']['SourcePrefix']+' ' + rss_data['link']
  return data 

if __name__ == '__main__':
  test_video = """
Xin Chun Kuai Le to my dear friends in China! Follow <a href="https://weibo.com/n/GranityStudios">@GranityStudios</a> to discover all the New Year gifts from me. <a data-url="http://t.cn/A6P4vrdP" href="https://video.weibo.com/show?fid=1034:4464353139949610" data-hide>KobeBryant的微博视频</a> <br><video src="http://f.video.weibocdn.com/0007wH7vlx07ApA2w7Fu010412004Apj0E010.mp4?label=mp4_hd&template=852x480.25.0&trans_finger=62b30a3f061b162e421008955c73f536&ori=0&ps=1CwnkDw1GXwCQx&Expires=1596472597&ssig=jdYuH97zC0&KID=unistore,video" controls="controls" poster="https://wx4.sinaimg.cn/orj480/c28dca85ly1gb7wzu6nolj21hc0u0gp6.jpg" style="width: 100%"></video>
"""
  print(TweetDecoder(test_video))
