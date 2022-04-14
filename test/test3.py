import time

import threading

# 字典
# PHP 数组
# request = {key1:value2,key2:value2...}
# 多线程 唯一标识
# request = {thread_key1:Request1, ....}
# id号
# 线程隔离

def worker():
    print('i am thread')
    t = threading.current_thread()
    print(t.getName())

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name='my_thread')
new_t.start()


# 更加充分的利用CPU的性能优势
# 异步编程
# 单核CPU
# 4核 A核 B核 并行的执行程序
# python不能充分利用多核CPU优势
# python的多线程是鸡肋
# 6 6 = 6
# GIL 全局解释器锁 global interpreter lock
# 锁 线程安全

# 内存资源 一个进程 有多个线程 共享
# 线程不安全

# a = 3

# A a+=1
# print(a)

# B a+=1
# print(a)

# 锁
# 细粒度锁 程序员 主动加锁
# 粗粒度锁 解释器 GIL 多核cpu 1个线程执行 一定程度上保证线程安全
# a+=1
# bytecode
# python cpython jpython
# 多进程 进程通信技术
t = threading.current_thread()
print(t.getName())


# 主线程

