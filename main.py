#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time,psutil
from myChrome import MyChrome
import global_log
from websites.wuhan_lvyouwei import Wuhan_lvyouwei

g_logger = global_log.myLogging().GetLog()

def WaitForbrowser(browserexe,time_seconds):
	while True:
		p_name = [psutil.Process(i).name() for i in psutil.pids()]#罗列进程的程序
		if browserexe in p_name:
			g_logger.info(browserexe + " has started")
			break
		else:
			g_logger.info("waitfor" + browserexe + " starting")
		time.sleep(time_seconds)


def main():
	#检测chrome启动后才往下执行
	WaitForbrowser('chrome.exe',1)
	input('请先在浏览器中登录账号后，点任意按键确认')
	g_logger.info("system start control your browser...")

	#启动driver
	driver = MyChrome().Work()	

	#打开主页
	wuhan_lvyouwei = Wuhan_lvyouwei()
	driver.get(wuhan_lvyouwei.urls[0])

	#根据关键字定位网页
	for keyword in wuhan_lvyouwei.keywordToUrl:
		element = driver.find_element_by_xpath("//*[contains(text(),'" + keyword + "')]")
		if element:
			element.click()

			#保存url
			if driver.current_url not in wuhan_lvyouwei.urls:
				wuhan_lvyouwei.urls.append(driver.current_url)
		else:
			g_logger.error("find_element_by_xpath:failed " + keyword)

		#切新主页
		driver.get(wuhan_lvyouwei.urls[0])
	g_logger.info(wuhan_lvyouwei.urls)
	

if __name__ == '__main__':
	main()