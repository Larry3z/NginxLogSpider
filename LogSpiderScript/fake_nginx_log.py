#!/usr/bin/env python
# coding=utf-8

from Logger import *
from get_product_url import *
from browser import *

def main():
    urls = get_product_urls();
    ip_file = open("real_ip.txt")
    logger = Logger("fake_nginx_log.log", logging.INFO, logging.DEBUG)
    logger.info("#########################Begin faking nginx log#########################")
    for line in ip_file:
        line = line.strip("\n")
        tmp = line.split("|")
        protocol = tmp[0].lower()
        """
        # ip = tmp[1].split("://")[1]
        # ip前面必须加上http或者https，不然windows下面不报错，linux下有问题
        # proxies = {
        # 'http': 'http://10.10.1.10:3128',
        # 'https': 'http://10.10.1.10:1080',
        # }
        # requests.get('http://example.org', proxies=proxies)
        """
        ip = tmp[1].strip("\r\n")
        proxy = {protocol: ip}
        try:
            for i in range(1, 10):
                headers = {"User-Agent": choice(user_agent)}
                requests.get(choice(urls), headers=headers, proxies=proxy, timeout=1)  # 这块会造成日志有问题
                logger.info("Fake log success! IP addr is " + ip + "!")
        except Exception, e:
            logger.error("ConnectionError!!! IP is " + ip + ".")
    logging.info("#########################Finish faking nginx log.#########################")
    ip_file.close()


if __name__ == "__main__":
    main()
