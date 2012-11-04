#!/usr/bin/python
# -*- encoding: utf-8 -*-

def fibonacci(n):

	a, b = -1, 1
	while n > 0:
		c = a + b
		yield c
		a, b = b, c
		n -= 1


