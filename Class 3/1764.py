'''
Date: 2024.07.08
No: 1764
Tier: Sliver 4
Name: 듣보잡
Language: Python 3
'''

import sys 

n, m = map(int, sys.stdin.readline().rstrip().split())
nlist = [] 
result = []
for i in range(n):
	nlist.append(sys.stdin.readline().rstrip())

nset = set(nlist) # 두 그룹간 중복된 요소를 찾아야 할떈 집합을 이용하면 더 빨리 해결 할 수 있음.
d = len(nset)
for i in range(m):
	temp = sys.stdin.readline().rstrip()
	nset.add(temp)
	if d == len(nset):
		result.append(temp)
	else:
		nset.discard(temp)

result.sort()

print(len(result))
for i in result:
	print(i)