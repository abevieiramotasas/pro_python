#!/usr/bin/python
# -*- encoding: utf-8 -*-

a = set(range(100))
b = set(x**2 for x in range(10))

print('uniao: %s' % str(a|b))
print('intersect: %s' % str(a&b))
print('diference: %s' % str(a-b))
print('sim diference: %s' % str(a^b))
print('is subset: %s' % b.issubset(a))

