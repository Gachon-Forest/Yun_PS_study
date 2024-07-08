'''
Date: 2024.07.08
No: 2751
Tier: Sliver 5
Name: 수 정렬하기 2
Language: Python 3
'''
import sys

#파이썬 sort는 진짜 개 사기다 22

N = int(input())
temp = []
for _ in range(N):
    temp.append(int(sys.stdin.readline()))
    # input()과 sys.stdin.readline()의 시간 차이가 매우 많이 남
    # 그러니 시간 초과가 뜬다면 일단 input()을 sys.stdin.readline()으로 바꿔보자.

for i in sorted(temp):
    print(i)