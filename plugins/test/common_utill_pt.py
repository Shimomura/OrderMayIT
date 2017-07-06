# -*- coding: utf-8 -*-
from plugins.common.common_utill import common_utill

def split_options_test(arg):
    dic = commonutill.split_options(arg)
    print (len(dic))
    for k,v in dic.items():
        print('key:' + str(k))
        print('val:' + str(v))

    dic = {}
    for k,v in dic.items():
        print('key:' + str(k))
        print('val:' + str(v))

split_options_test("b -a c")
