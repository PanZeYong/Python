#!/usr/bin/env python3
# print("Hello, Python");

# print(12 * 13);

# 输入
# name = input("please input what you want to : ");
# print("Hello", name);

# a = input("please input age");
# a = ord(a);
# if a >= 0:
# 	print(a);
# else :
# 	print(-a);

# print("字符串制表符\t换行\n\\");
		
# b = "ABC";
# c = b;
# b = "Python";
# print(c);

# n = 123;
# f = 456.789;
# s1 = "Hello, world";
# s2 = "Hello, \'Adam\'";
# s3 = r'Hello, "Bart"';
# s4 = r'''Hello,
# Lisa!''';
# print(n);
# print(f);
# print(s1);
# print(s2);
# print(s3);
# print(s4);

# x = (85 - 72) / 72;
# print("小明的成绩提高：","%.1f" % x);

# score = input("请输入您的成绩：");
# score = int(score);
# if score >= 90:
# 	print("优秀");
# elif score >= 80:
# 	print("良好");
# elif score >= 70:
# 	print("不错");
# elif score >= 60:
# 	print("及格");
# else:
# 	print("不及格，继续努力");

# height = 1.73;
# weight = 55;
# bmi = weight / height /  height;
# print("BMI : ",bmi);
# if bmi > 32:
# 	print("严重肥胖");
# elif bmi > 28 and bmi <= 32:
# 	print("肥胖");
# elif bmi > 25 and bmi <= 28:
# 	print("过重");
# elif bmi > 18.5 and bmi <= 25:
# 	print("正常");
# else:
# 	print("过轻");

# languages = ["PHP", "JAVA", "PHP", "Ruby", "Object-C"];
# print("----------Programming Language----------");
# for language in languages:
# 	print(language);

# print("----------Sum---------");
# sum = 0;
# for x in range(200):
# 	sum = sum + x;
# print(sum);

# while True:
# 	print("Python");

# 判断数据类型（isinstance）
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError("bad operand type");
	if x >= 0:
		return x;
	else:
		return -x;

# 函数返回多个值，但其实是tuple

import math

def mov(x, y, step, angle=0):
	nx = x + step * math.cos(angle);
	ny = y - step * math.sin(angle);
	return nx, ny;

def quadratic(a, b, c):
	if not isinstance(a, (int, float)) & isinstance(b, (int, float)) & isinstance(c, (int, float)):
		raise TypeError("Wrong data type");
	else:
		temp = b * b - 4 * a * c;
		if temp > 0:
			return (-b + math.sqrt(temp)) / (2 * a),(-b - math.sqrt(temp)) / (2 * a);
		elif temp == 0:
			return (-b) / (2 * a);
		else:
			print("无解");

# 位置参数
def power(x, n):
	s = 1;
	while n > 0:
		n = n - 1;
		s = s * x;
	return s;

#默认参数
# 1. 必选参数在前，默认参数在后 
# 2. 当函数有多个参数时，把变化大的参数放在前面，变化小的参数放在后面，变化小的参数作为默认参数
# 3. 多个调用参数调用顺序，按照顺序调用时，按照指定顺序调用，没有的就用默认值；不按照顺序调用时，指定相应参数名调用
# 4. 默认参数必须指向不变对象（可用 None）
# 5. 降低函数调用的难度
def power(x, n=2):
	s = 1;
	while n > 0:
		n = n - 1;
		s = s * x;
	return s;

def enroll(name, gender, age=6, city="ZhuHai"):
	print("name : ", name);
	print("gender : ", gender);
	print("age : ", age);
	print("city : ", city);

def add_end(L = None):
	if L is None:
		L = [];
	L.append("END");
	return L;

# 可变参数
# 1. 与定义一个 list 或者 tuple 参数相比，定义可变参数只需在参数面前加上 *
# 2. 在 list 或者 tuple 前面加上 * 就可以转换为可变参数
# 3. 可变参数在函数调用自动被组装为tuple

# 定义 list 参数或者 tuple参数
def calc(numbers):
	sum = 0;
	for n in numbers:
		sum = sum + n * n;
	return sum;

# 定义可变参数
def calc(*numbers):
	sum = 0;
	for n in numbers:
		sum = sum + n * n;
	return sum;

# 关键字参数
# 1. 0个或任意个含参数名的参数，关键字参数在函数调用时自动组装为dict
# 2. 关键字参数用 **keyword 表示
# 3. 可以组装dict，然后通过 ** 将其转换为关键字参数

def person(name, age, **kw):
	print("name : ", name, "age : ", age, "keyword : ", kw);

# 命名关键字参数
# 1. 以 * 为特殊分隔符，* 后面的参数为命名关键字参数
# 2. 如果函数定义中已经有可变参数，命名关键字参数就不需要 * 作为分隔符了
# 3. 必须指定参数名，即键值对
def person(name, age, **kw):
	if "city" in kw:
		pass;

	if "job" in kw:
		pass;

	print("name : ", name, "age : ", age, "keyword : ", kw);

def person(name, age, *, city, job):
	print(name, age, city, job);

# 参数组合
# 1. 参数定义顺序：必选参数、默认参数、可变参数、命名关键字参数、关键字参数

def f1(a, b, c=0, *args, **kw):
	print("a:",a, "b:", b, "c:", c, "args:", args, "kw:", kw);

# 汉诺塔

def move(n, a, b, c):
	if n == 1:
		print("a ---> c");
	else:
		move(n-1, a, c, b);
		print("a ---> b");
		move(1, a, b, c);
		print("a ---> c");
		move(n-1, b, a, c);
		print("b ---> c");

















