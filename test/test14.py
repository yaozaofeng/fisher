"""
 Created by 七月 on 2018-4-16.
"""
__author__ = '七月'


def intro(list):
    intros = filter(lambda x: True if x else False,
                    list)

    return ' / '.join(intros)

print(intro(['1',False,'3']))
