# -*- coding: utf-8 -*-
from hello import Hello
h = Hello()
h.hello()
print(type(Hello))
print(type(h))


def fn(self, name='world'):
    print('Hello, %s' % name)

Hello2 = type('Hello', (object, ), dict(hello=fn))
h2 = Hello2()
h2.hello()
print(type(Hello2))
print(type(h2))


class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
# L2 = list()
# L2.add(1)
