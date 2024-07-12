'''
Date: 2024.07.12
No: 1003
Tier: Sliver 3
Name: 피보나치 함수
Language: Python 3
'''

# 제한 시간이 0.25초라 단순히 0, 1 나올떄마다 1 더하는 방식은 시간 초과가 뜸.
# DP를 사용해서, 미리 계산된 내용은 더해주는 방식으로 가면 괜찮을 듯?

import sys

f = [[-1,0,0] for _ in range(41)] #값을 미리 저장할 값
f[0] = [0,1,0]
f[1] = [1,0,1]

def fibo(n:int) -> list:
	if n == 0:
		return f[0][0]
	elif n == 1:
		return f[1][0]

	elif f[n][0] != -1: # 만약 이미 한번 계산을 했었을 경우, 저장된 값을 불러옴
		return f[n][0]

	else:
		val = fibo(n-1) + fibo(n-2)
		zc = f[n-1][1] + f[n-2][1]
		oc = f[n-1][2] + f[n-2][2]
		f[n] = [val, zc, oc] #피보나치 값, 0 호출 수, 1 호출 수
		return f[n][0]

t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	fibo(n)
	print(f[n][1], f[n][2])
