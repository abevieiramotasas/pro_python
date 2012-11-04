#!/usr/bin/python
# -*- encoding: utf-8 -*-

# decorator sem param

def print_exec_time(func):

	def wrapper(*args, **kwargs):
		from datetime import datetime
		init_time = datetime.now()
		func(*args, **kwargs)
		exec_time = datetime.now() - init_time
		print('Tempo de execução = %d' % exec_time.total_seconds())

	return wrapper

# decorator com param

def print_exec_time_message(message='Tempo de execução = %d'):

	def _print_exec_time_message(func):

		def wrapper(*args, **kwargs):
			from datetime import datetime
			init_time = datetime.now()
			func(*args, **kwargs)
			exec_time = datetime.now() - init_time
			print(message % exec_time.total_seconds())
		
		return wrapper
	return _print_exec_time_message

	
def memoize(func):

	cache = {}
	def wrapper(*args):
		if args in cache:
			print('usou cache')
			return cache[args]

		result = func(*args)
		cache[args] = result
		return result
	return wrapper

