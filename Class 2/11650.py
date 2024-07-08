'''
Date: 2024.07.08
No: 11650
Tier: Sliver 5
Name: 좌표 정렬하기
Language: Python 3
'''

# 정렬 문제를 풀다보니 금방 풀었다.   
# 주어진 정렬 조건의 역순으로 정렬을 진행하면 된다.

import sys

n = int(input())
temp = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split()) 
    temp.append([x, y])

# 문제 -> x 값 기준으로 정렬(1), 만약 x값이 같으면 y값 기준으로 정렬(2)
temp.sort(key = lambda x : x[1]) #(2) y값 기준으로 선 정렬 후
temp.sort(key = lambda x : x[0]) #(1) x값 기준으로 정렬


for arr in temp:
    print(arr[0], arr[1])

