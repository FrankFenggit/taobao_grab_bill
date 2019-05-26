#!/usr/bin/python
import time,psutil
from myChrome import MyChrome
import global_log

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
		pass

def main():
	#检测chrome启动后才往下执行
	WaitForbrowser('chrome.exe',1)
	driver = MyChrome().Work()

	driver.get('https://detail.tmall.com/item.htm?id=588093164780&spm=a21bz.7725273.1998564503.1.77d33db8oo42nh&umpChannel=qianggou&u_channel=qianggou')
	

if __name__ == '__main__':
	main()