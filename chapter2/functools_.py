#!/usr/bin/python
# -*- encoding: utf-8 -*-

import functools

# partial

def pre_fix(word, prefix):
	return prefix+word

pre_fix_in = functools.partial(pre_fix, prefix='in')

print(pre_fix_in(word='util'))
