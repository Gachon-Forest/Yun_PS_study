'''
Date: 2024.07.07
No: 1546
Tier: Bronze 1
Name: 평균
Language: Python 3
'''

n = int(input()) 
score = list(map(int, input().split()))
max_score = max(score)
avr = 0
for i in score:
  avr += i/max_score * 100

print(avr/n)