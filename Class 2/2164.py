'''
Date: 2024.07.08
No: 2164
Tier: Sliver 4
Name: 카드2
Language: Python 3
'''
n = 1
import sys
def c(n):
    if n < 1000: # 1000이하는 그냥 계산 가능함.
        card = [i for i in range(1, n+1)]
        while(len(card) != 1):
            del card[0]
            temp = card.pop(0)
            card.append(temp)
        return card[0]

    elif n % 2 == 0: # 짝수일 경우
        return c(n//2) * 2 #n/2한 값에 * 2

    else: # 홀수일 경우
        t = c(n-1) + 2 
        if t > n: #가끔 2로 초기화 되는 부분이 있음 (ex: 129) 예외처리 부분
            return 2
        else:
            return t

n = int(input())
print(c(n))