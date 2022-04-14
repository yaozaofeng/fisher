"""
 Created by 七月 on 2018-4-13.
"""
from math import floor


def test():
    while True:
        receive = input()
        gift = input()
        a = True if floor(int(receive) / 2) <= floor(int(gift)) else False
        print(a)


test()
