# -*- coding: utf-8 -*-
import functools


def int2(x, base=2):
    return int(x, base)


print(int2('100000'))

# 有了偏函数，就不需要自定义int2()
# 偏函数就是把一个函数的某些参数给固定住，返回一个新的函数
int2 = functools.partial(int, base=2)
print(int2('1000000'))


int2 = functools.partial(int, base=2)

