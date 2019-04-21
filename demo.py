#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'urlget module '

__author__ = 'yuan meng'

from urllib import request
import ssl
url = 'https://www.douban.com/'

ssl._create_default_https_context = ssl._create_unverified_context
def cusget():
	with request.urlopen(url) as f:
	    # get请求
	    data = f.read()
	    #打印状态行
	    print('Status:', f.status, f.reason)
	    #打印响应头
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', data.decode('utf8'))


if __name__=='__main__':
	cusget()
