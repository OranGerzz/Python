#! usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Q
import time
import psutil

# def get_key():
#
#     key_info = list(psutil.net_io_counters(pernic=True).keys())
#     recv = {}
#     sent = {}
#     recv.setdefault(key_info[0],psutil.net_io_counters(pernic=True).get(key_info[0]).bytes_recv)
#     sent.setdefault(key_info[0],psutil.net_io_counters(pernic=True).get(key_info[0]).bytes_sent)
#
#     print(recv)
#     print(sent)
#
#     return key_info, recv, sent
#
#
# get_key()
a=1
b=2
c=3
def test(ab):
    a,b,c = ab()
    print(ab)
test()