'''
Date: 2024.07.07
No: 2562
Tier: Bronze 3
Name: 최댓값
Language: Python3
'''
a = []
for i in range(9):
	a.append(int(input()))
print(max(a))
print(a.index(max(a)) + 1)
