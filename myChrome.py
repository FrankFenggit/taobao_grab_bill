#!/usr/bin/python
# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class MyChrome(object):
	"""docstring for MyChrome"""
	def __init__(self):
		super(MyChrome, self).__init__()
		self.chrome_options = Options()
		self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
		# driver就是当前浏览器窗口
		

	def Work(self):
		self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
		return self.driver
