#-*- coding:utf-8 -*-
from selenium import webdriver
from scrapy.http import HtmlResponse
from lxml import etree
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from random import choice

# 用户代理列表
ua_list = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36"
]

# 配置 Chrome 无头浏览器
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("user-agent={}".format(choice(ua_list)))

# 初始化 WebDriver
driver = webdriver.Chrome(options=options)

class SeleniumMiddleware(object): 
    def process_request(self, request, spider):
        print(spider.name)
        try:
            driver.get(request.url)
            driver.implicitly_wait(3)
            time.sleep(5)
            page = driver.page_source  # 获取页面源码
            close_driver()

            return HtmlResponse(request.url, body=page, encoding='utf-8', request=request)
        except:
            print("Error fetching data for spider: {}".format(spider.name))

def close_driver():
    driver.close()

