#!/usr/bin/env python
# coding=utf-8

"""
从xiciD代理网站爬取高匿IP后，很多IP不一定是可以使用的所以需要去验证一下
"""
from random import choice

import requests
from Logger import *

from browser import *

url = "http://ip.chinaz.com/getip.aspx"
logger = Logger("test_xici_ip.log", logging.INFO, logging.DEBUG)


def testIP(url, header, proxy, timeout):
    try:
        resp = requests.get(url, headers=header, proxies=proxy, timeout=timeout, allow_redirects=False)
        logger.info(resp.content)
        return 1
    except Exception, e:
        logger.error("ConnectionError")
        return 0


def getIPs():
    all_ip = []
    ip_file = open("xici_ips.txt")
    try:
        for line in ip_file:
            line = line.strip("\n")
            all_ip.append(line)
    finally:
        return all_ip
        ip_file.close()


def collectRealIp():
    headers = {"user-agent": choice(user_agent)}
    real_ip_file = open("real_ip.txt", "w")
    all_ip = getIPs()
    logger.info("######################### Begin testing xici ip #########################")
    for line in all_ip:
        line = line.split("|")
        protocol = line[0]
        ip = line[1].split("://")[1]
        proxy = {protocol.lower(): ip,}
        result = testIP(url, headers, proxy, 0.5)
        if result == 1:
            logger.info("good ip " + ip)
            real_ip_file.write("%s|%s://%s\n" % (protocol, protocol, ip))
    logger.info("######################### Finish testing xici ip #########################")
