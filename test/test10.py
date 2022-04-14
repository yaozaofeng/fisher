"""
 Created by 七月 on 2018-2-23.
"""
__author__ = '七月'


class A:
    def _get_b(self):
        return 1


class B(A):
    def __init__(self):
        A.__init__(self)

    def go(self):
        return self.b


print(B().go())
