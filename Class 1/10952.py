'''
Date: 2024.07.07
No: 10952
Tier: Bronze 5
Name: A+B - 5
Language: Python3
'''
while(True):
	a, b = map(int, input().split())
	if(a == 0 and b == 0):
		break
	print(a + b)