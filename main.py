#!/usr/bin/python
# -*- coding: UTF-8 -*-

from myChrome import MyChrome

def main():
	driver = MyChrome().Work()

	driver.get('https://detail.tmall.com/item.htm?id=588093164780&spm=a21bz.7725273.1998564503.1.77d33db8oo42nh&umpChannel=qianggou&u_channel=qianggou')
	

if __name__ == '__main__':
	main()