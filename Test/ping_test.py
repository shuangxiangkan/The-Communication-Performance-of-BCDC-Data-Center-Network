#! /usr/bin/env python
import os

if(os.system(r'ping www.baidu.com')==0):
    print('OK')
else:
    print('Connection failed')
