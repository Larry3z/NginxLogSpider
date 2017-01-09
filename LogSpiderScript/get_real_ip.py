#!/usr/bin/env python
# coding=utf-8

"""
获取IP并验证可用性，之所以放到两个类里面是因为IP代理网站会封IP，分开了好测试
"""

from test_xici_ip import *

from xici_ip_crawler import *


def main():
    xici_url = "http://www.xicidaili.com/nn/"# 这个网站的IP不少都是失效的，只爬第一页的就够了
    ip_crawler(xici_url)
    collectRealIp()


if __name__ == "__main__":
    main()
