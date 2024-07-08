'''
Date: 2024.07.07
No: 11723
Tier: Sliver 5
Name: 집합
Language: Python 3
'''

# sys.stdin.readline()을 이용하면, 입력시 걸리는 시간을 줄일 수 있다.
# 타임 아웃을 피해갈 수 있는 테크닉이므로 외워둘 것.

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1: #all와 empty의 경우, 숫자가 입력되지 않으므로 리스트의 크기는 1임
        if temp[0] == "all": # all일 경우
            S = set([i for i in range(1, 21)]) # 집합에 모든 원소를 집어 넣음
        else: #empty 일 경우
            S = set() # 집합을 공집합으로 초기화 함
    
    else:
        func, x = temp[0], temp[1] #temp[0] = 명령어, temp[1] = 인자
        x = int(x) # int로 형변환

        if func == "add":
            S.add(x) 
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)