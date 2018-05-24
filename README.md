pycharm里运行start.py会出现两个问题
1、ImportError: No module named win32api
   需要安装Py32Win模块
   简便的做法就是：pip install pypiwin32
2、DEBUG: Ignoring response <403 http://movie.douban.com/top250>: HTTP status code is not handled or not allowed 
   在settings.py里加上USER_AGENT：
   USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'  