# -*- coding: utf-8 -*-
print(list(range(1,11)))

# 1,11里求平方
print([x * x for x in range(1,11)])

# 偶数求平方
print([ x * x for x in range(1, 11) if x % 2 == 0 ])

# 两层循环做全排列
print( [m + n for m in 'ABC' for n in 'XYZ'])

# 拿出当前文件所在目录的所有文件和目录名
import os
print( [d for d in os.listdir('.')] )

# 循环同时使用两个甚至多个变量， 比如dict的items可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量生成list：
print( [k + '=' +v for k, v in d.items()] )
