# weibo2toot

A simple script that transport Weibo content to Mastodon. Based on the Weibo RSS feed powered by [RSSHub](https://rsshub.app).

一个将微博搬运到长毛象的脚本——基于[RSSHub](https://rsshub.app)生成的B站动态RSS。

<details>
  <summary>一些说明</summary>
  
  1、微博视频有严格的反盗链措施，一定频率内请求次数过多可能导致请求返回403，所以输出中看到视频下载失败问题不大，默认情况下会用视频缩略图顶替，视频原链接会在嘟文中标出（完全保留微博风格）。

  2、`TypeError: Cannot read property 'screen_name' of undefined`  
  这是一个 RSSHub 方面的问题，部分微博博主的内容需要登陆才可见，不支持订阅，可以通过打开 https://m.weibo.cn/u/:uid 验证。

  3、表情处理：微博表情暂时没有找到好的索引及批处理的方式（我们需要先将表情批量扒下来并上传为Mastodon的自定义表情），所以目前暂时还没法处理表情。
</details>

```
pip3 install -r requirements.txt
cp conf.sample.ini conf.ini
nano conf.ini
python3 run.py
```

crontab job setting:
```
crontab -e
```
or (Ubuntu 18.04)
```
nano /etc/crontab
/etc/init.d/cron restart
```

Recommand do job hourly:
```
#m h dom mon dow user  command
13 *    * * *   root    cd /weibo2toot && python3 run.py
```
