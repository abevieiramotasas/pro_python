#!/usr/bin/python
# -*- encoding: utf-8 -*-

from collections import defaultdict

# produz um dictionary que retorna um valor default
# caso não possua valor para a chave

def count_words(w):
	count = defaultdict(int)
	for word in w.split():
		count[word] += 1
	return count


print(count_words('Abelardo Vieira Mota'))
print(count_words('Abelardo Abelardo'))
