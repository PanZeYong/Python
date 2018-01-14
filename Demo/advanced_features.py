#!/usr/bin/env python3

# list 切片
# 注意：[-3:-1] 与 [-3:] 区别
# 1. [a : b : c]：以 a 为起点，前 b 个数取一个
def slice():
	L = ["Jack", "John", "Marry", "Jeep", "Jim"];
	print(L[0:3]);
	print(L[-3:-1]);
	print(L[-3:]);

# 迭代 
def iteration():
	d = {"a":1, "b":2, "c":3};
	for key in d:
		print(key);
	for value in d.values():
		print(value);
	for key, value in d.items():
		print(key,value);

# 判断一个对象是否是可迭代对象
import collections

def iterable():
	# print(isinstance("abcde", Iterable));
	# print(isinstance([1, 2, 3, 4], Iterable));
	# print(isinstance(1234, Iterable));
	
	for i, value in enumerate(['A', 'B', 'C']):
		print(i, value);

import os
# 列表生成式
def listComprehensions():
	L = list(range(1, 21));
	print(L);
	print('生成平方：x*x');
	print([x * x for x in range(1, 20)]);
	print([x * x for x in range(1, 20) if x % 2 == 1]);
	print([m + n for m in "ABCD" for n in "EFG"]);
	print([d for d in os.listdir()]);

def letters():
	L = ['Java', 18, 'PHP', 21, 22, 'Python', 'Object-C'];
	print([s.lower() for s in L if isinstance(s, str)]);

# 生成器 generator
# 1. 把列表生成式 [] 改为 ()
# 2. 如果一个函数定义中包含 yield 关键字，那么该函数不是普通函数，而是 generator
# 3. 执行顺序与普通函数有区别，遇到 yield 就返回，再次执行时从上次 yield 返回的语句开始
# 4. 用 for 循环调用 generator时，拿不到 return 返回值，需要捕获 StopIteration 异常，因为返回值是包含在 StopIteration 中 value
def g():
	g = (x * x for x in range(1, 20));
	for n in g:
		print(n);

# 斐波拉契数列
def fib(max):
	n, a, b = 0, 0, 1;
	while n < max:
		yield b;
		a, b = b, a+b;
		n = n + 1;
	return 'done';

n = fib(8);
while True:
	try:
		x = next(n);
		print('g:', x);
	except StopIteration as e:
		print('Generator return value', e.value);
		break;

def odd():
	print('step 1');
	yield 1;
	print('step 2');
	yield 3;
	print('step 3');
	yield 5;

# 迭代器
# 1. 可迭代对象（Iterable）：直接作用于 for 循环的对象，比如 list、tuple、dict、set、str
# 2. 迭代器（Iterator）：被 next() 函数调用并不断返回下一个值的对象，比如 generator 和带 yield 的生成器函数
# 3. 生成器都是 Iterator 对象，但 list、tuple、dict、set、str 是 Iterable 对象，却不是 Iterator 对象， 可以通过 iter() 函数转换































