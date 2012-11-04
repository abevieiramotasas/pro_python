#!/usr/bin/python
# -*- encoding: utf-8 -*-

from collections import OrderedDict

# ordereddict preserva a ordem original das keys

d = OrderedDict((x, x**2) for x in range(10))
d[11] = 121
d[10] = 100
print(d)
print(d.keys())
