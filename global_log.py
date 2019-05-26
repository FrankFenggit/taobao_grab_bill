#!/usr/bin/python
# -*- coding: UTF-8 -*-

import logging  # 引入logging模块
import os.path
import time


# g_logger.debug('this is a logger debug message')
# g_logger.info('this is a logger info message')
# g_logger.warning('this is a logger warning message')
# g_logger.error('this is a logger error message')
# g_logger.critical('this is a logger critical message')

class myLogging(object):
	"""docstring for myLogging"""
	__logger = None
	def __init__(self):
		super(myLogging, self).__init__()
	def GetLog(self):
		if myLogging.__logger:
			pass
		else:
			# 第一步，创建一个logger
			myLogging.__logger = logging.getLogger()
			myLogging.__logger.setLevel(logging.INFO)  # Log等级总开关
			# 第二步，创建一个handler，用于写入日志文件
			rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
			log_path = os.path.dirname(os.getcwd()) + '/Logs/'
			print('log path:   '+log_path)
			log_name = log_path + rq + '.log'
			logfile = log_name
			fh = logging.FileHandler(logfile, mode='w')
			fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
			#插入控制台输出
			ch = logging.StreamHandler()
			ch.setLevel(logging.INFO)  # 输出到console的log等级的开关
			# 第三步，定义handler的输出格式
			formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
			fh.setFormatter(formatter)
			ch.setFormatter(formatter)
			# 第四步，将logger添加到handler里面
			myLogging.__logger.addHandler(fh)
			myLogging.__logger.addHandler(ch)

		return myLogging.__logger

