#coding:utf-8

#第一个例子：递归求总和.出口为n=1
def ksum(n):
	if n==1:
		return 1
	else:
		result = n+ksum(n-1)
		return result
print(ksum(100))

#第二种递归写法
def kksum(n):
	if n>0:
		return n +kksum(n-1)
	else:
		return 0
print(kksum(100))

#第三种递归写法
def kkksum(n):
	if n==0:
		return 0
	else:
		return n+kkksum(n-1)
print(kksum(100))

#第四种递归的写法
def k4sum(n):
	if n<0:
		return 0
	else:
		return n+k4sum(n-1)
print(k4sum(100))

#递归求阶乘
def product1(n):
	if n==1:
		return 1
	else:
		return n*product1(n-1)
print(product1(10))

#第二种写法
def product2(n):
	if n<=0:
		return 1
	else:
		return n*product2(n-1)
print(product2(10))

#第三种写法
def product3(n):
	if n>0:
		return n*product3(n-1)
	else:
		return 1
print(product3(10))

#递归求平方和
def sqrr(n):
	return n*n

