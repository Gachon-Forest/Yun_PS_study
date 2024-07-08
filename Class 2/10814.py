'''
Date: 2024.07.08
No: 10814
Tier: Sliver 5
Name: 나이순 정렬
Language: Python 3
'''
import sys

n = int(input())
temp = []
for i in range(n):
    age, name = sys.stdin.readline().split() # 시간 초과엔 sys.stdin.readline()이 직빵이다.
    temp.append([int(age), name])

temp.sort(key = lambda x : x[0]) 
#2차원 리스트의 0번째 인덱스를 기준으로 정렬, 
#lambda 식은 잘 사용할 수 있도록 연습하자.

for arr in temp:
    print(arr[0], arr[1])

