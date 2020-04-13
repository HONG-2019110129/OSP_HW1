#!/usr/bin/python

n = int(input("fibonacci number?: "))

fibo = [1,1]
for i in range(2, n):
	f1 = fibo[i-2]
	f2 = fibo[i-1]
	fibo.append(f1 + f2)

for a in fibo:
	print(a, end=",")

print("")
print("F%d = %d" %(n,a))
