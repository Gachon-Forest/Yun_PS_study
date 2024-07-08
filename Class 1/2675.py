'''
Date: 2024.07.07
No: 2675
Tier: Bronze 3
Name: 문자열 반복
Language: Python3
'''
T = int(input())
for i in range(T):
  n = list(input().split(" "))
  for i in n[1]:
    for j in range(int(n[0])):
      print(i, end = "")
  print("")
