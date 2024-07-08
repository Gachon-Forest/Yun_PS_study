'''
Date: 2024.07.07
No: 2609
Tier: Bronze 1
Name: 최대공약수와 최소공배수
Language: Python 3
'''

# 수학을 공부해야 하는 EU

def gcd(a, b): #유클리드 호제법. 최대 공약수 어쩌구 나오면 이거부터 만들고 시작하자.
    while b > 0:
        a, b = b, a % b
    return a

a,b = map(int, input().split())
s = gcd(a, b)
l = (a * b // s) #최소 공배수는 a * b // gcd(a, b)로 구할수 있다.
print(s)
print(l)

