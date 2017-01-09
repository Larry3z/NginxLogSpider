#!/usr/bin/env python
# coding=utf-8


"""
从xiciD代理网站爬取高匿IP，通过http://ip.chinaz.com/getip.aspx确定IP是否失效
把没失效的IP储存起来，用来伪造NGINX日志
"""
from random import choice

import requests
from Logger import *
from bs4 import BeautifulSoup
from browser import *

logger = Logger("xici_ip_crawler.log", logging.INFO, logging.DEBUG)


def ip_crawler(url):
    ip_file = open("xici_ips.txt", "w")
    headers = {"User-Agent": choice(user_agent)}
    resp = requests.get(url, headers=headers, timeout=5)
    content = resp.content
    soup = BeautifulSoup(content)
    trs = soup.find("table", {"id": "ip_list"}).findAll("tr")
    logger.info("#########################Begin collecting ips from www.xicidaili.com#########################")
    for tr in trs[1:]:
        tds = tr.findAll("td")
        ip = tds[1].text.strip()
        port = tds[2].text.strip()
        protocol = tds[5].text.strip()
        if protocol == "HTTP" or protocol == "HTTPS":
            ip_file.write("%s|%s://%s:%s\n" % (protocol, protocol, ip, port))
            logger.info("%s://%s:%s" % (protocol, ip, port))
    logger.info("#########################Finish collecting ips from www.xicidaili.com#########################")
