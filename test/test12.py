"""
 Created by 七月 on 2018-4-4.
"""
__author__ = '七月'


class A():
    def __call__(self):
        return object()

class B():
    def run(self):
        return object()

def func():
    return object()

def main(callable):
    callable()
    # 我想在main中调用传入的参数，得到一个对象object
    # b.run()
    # a.go()
    # func()
    # ...
    pass

main(A())
main(B())
main(func)
