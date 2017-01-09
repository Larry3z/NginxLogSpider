#!/usr/bin/env bash
echo "*/5 * * * * root /home/software/nginx_spider/fakeLog.sh" >> /etc/crontab

#通过cron表达式执行python脚本会造成当前目录的变化，所以会导致python找不到文件了
#每分钟伪造一下日志
*/1 * * * * root  cd /home/software/LogSpider/LogSpiderScript && /usr/local/python2.7/bin/python2.7 /home/software/LogSpider/LogSpiderScript/fake_nginx_log.py
#4个小时更新一下ip
0 */4 * * * root  cd /home/software/LogSpider/LogSpiderScript && /usr/local/python2.7/bin/python2.7 /home/software/LogSpider/LogSpiderScript/get_real_ip.py
