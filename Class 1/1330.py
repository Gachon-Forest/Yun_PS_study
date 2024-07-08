'''
Date: 2024.07.07
No: 1330
Tier: Bronze 5
Name: 두 수 비교하기
Language: Python3
'''
a, b = map(int, input().split())

if a == b:
	print("==")
else:
	print(">" if a > b else "<")
