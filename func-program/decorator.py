# -*- coding: utf-8 -*-
import functools


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s()' % func.__name__)
#         return func(*args, **kw)
#     return wrapper


# @log
# def now():
#     print('2015-3-15')


# now()
# 装饰器
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 带参数的log装饰器
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():') % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
