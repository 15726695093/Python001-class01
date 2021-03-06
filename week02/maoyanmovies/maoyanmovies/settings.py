# -*- coding: utf-8 -*-

# Scrapy settings for maoyanmovies project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from fake_useragent import UserAgent

BOT_NAME = 'maoyanmovies'

SPIDER_MODULES = ['maoyanmovies.spiders']
NEWSPIDER_MODULE = 'maoyanmovies.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'maoyanmovies (+http://www.yourdomain.com)'

ua = UserAgent(verify_ssl=False)
USER_AGENT = ua.random

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'maoyanmovies.middlewares.MaoyanmoviesSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'maoyanmovies.middlewares.MaoyanmoviesDownloaderMiddleware': 543,
   'maoyanmovies.middlewares.RandomHttpProxyMiddleware': 400
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'maoyanmovies.pipelines.MaoyanmoviesPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# 爬取电影数量
MOVIE_NUM = 10


# 代理服务器列表
HTTP_PROXY_LIST = [
   'http://119.254.94.93:44665',
   'http://27.72.29.159:8080',
   'http://212.129.3.228:5836',
   'http://47.244.235.213:80',
   'http://125.209.73.170:3128',
   'http://178.134.155.82:48146',
   'http://185.232.66.125:5836',
   'http://202.131.229.10:8080',
   'http://203.204.200.108:443',
   'http://212.115.224.71:53281'
   'http://52.179.231.206:80',
   'http://95.0.194.241:9090'
]


# Mysql 配置
MYSQL_CONFIG = {
   'host': 'localhost',
   'port': 3306,
   'user': 'root',
   'password': 'root',
   'charset': 'utf8mb4'

}


# 爬取结果存储方式(mysql/csv)
DATA_STORE = 'mysql'