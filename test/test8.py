"""
 Created by 七月 on 2018-2-22.
"""
__author__ = '七月'

from werkzeug.local import LocalStack

# push、pop、top

s = LocalStack()
s.push(1)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

s.push(1)
s.push(2)
# 栈 后进先出
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

# s[7] 栈、序列（列表）
# 数据结构 限制了某些能力

