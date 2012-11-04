#!/usr/bin/python
# -*- encoding: utf-8 -*-

from collections import namedtuple

Point = namedtuple('Point', 'x y')
p1 = Point(10, 20)
p2 = Point(20, 10)
print('p1 %s %s' %(p1.x, p1.y))
