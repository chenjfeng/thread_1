#coding:utf-8

#第一个例子：递归求总和.出口为n=1
def ksum(n):
	if n==1:
		return 1
	else:
		result = n+ksum(n-1)
		return result

print(ksum(100))

#第二个例子：递归求平方和
def kcount(n):
	if n==1:
		return 1
	else:
		return n*n +kcount((n-1)*(n-1))
print(kcount(3))