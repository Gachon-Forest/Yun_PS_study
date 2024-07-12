'''
Date: 2024.07.12
No: 11399
Tier: Sliver 4
Name: ATM
Language: Python 3
'''
import sys
t = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

sum = 0
temp = 0
for i in arr:
	temp += i # (p1) + (p2) + (p3) ..
	sum += temp# (p1)+ (p1+p2) + (p1+p2+p3) ... 

print(sum)

