'''
Date: 2024.07.12
No: 1463
Tier: Sliver 3
Name: 1로 만들기
Language: Python 3
'''

count = 0


import sys

t = int(sys.stdin.readline())

while(t != 1):
	if t // 3 == 0:
		t = t//3
		count += 1
	elif t // 2 == 0:
		t = t // 2
		count += 1
	else:
		t = t - 1
		count += 1

print(count)