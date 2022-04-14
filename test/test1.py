"""
 Created by 七月 on 2018-2-6.
"""
import threading

import time
from werkzeug.local import Local


class A:
    a = 1


a_obj = A()
local = Local()
local.obj = a_obj

def set_A():
    local.obj = a_obj
    local.obj.a = 2
    print('in thread'+ str(local.obj.a))

def set_B():
    a_obj.a = 2
    print('in thread'+ str(a_obj.a))

thr = threading.Thread(target=set_A)
thr.start()
time.sleep(2)
# set_A()
print('in main' + str(a_obj.a))


