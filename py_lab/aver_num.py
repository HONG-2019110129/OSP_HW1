#!/usr/bin/python

mysum = 0
n = int(input("How many number do you enter?:"))

for i in range(1,n+1):
	a = int(input("NUM%d= "%(i)))
	mysum+=a

print("average is %.2f"%(mysum/n))
