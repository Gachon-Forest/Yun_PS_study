'''
Date: 2024.07.08
No: 1920
Tier: Sliver 4
Name: 수 찾기
Language: Python 3
'''

import sys 

n = int(sys.stdin.readline())
nset = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))
d = len(nset)

for i in mlist: 
    # python in 함수는 반복문 돌리는거랑 같은 시간을 가진다.
    # 대신 set을 사용하면 좀 더 효율적으로 빠르게 진행할 수 있다.
    nset.add(i)
    if d == len(nset):
        print(1)
    else:
        print(0)
        nset.remove(i)