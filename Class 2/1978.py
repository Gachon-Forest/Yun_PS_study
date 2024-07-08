'''
Date: 2024.07.07
No: 1978
Tier: Bronze 2
Name: 소수 찾기
Language: Python 3 
'''

def isprime(num): # 소수 판별 함수
  if num == 1: # 1 != 소수
    return False 
  elif num == 2: # 2는 소수
    return True
  else: # 1, 2를 제외하면 특이 케이스가 없음(단 num  = 자연수)
    for i in range(2, num): #1과 자기 자신을 제외한 수로 나눠지면 안됨.
      if(num % i == 0): # 만약 나눠질 경우
        return False # 소수가 아님
    return True
# 해당 방식은 num 값이 크지 않을때만 사용할 것.
# 조금의 오차가 허용 된다면 밀러-라빈 소수 판별이나, 에라토스테네스의 체 사용할 것
# 수학 공부.... 해야겠지?

count = 0
n = int(input())
prime_list = list(map(int, input().split())) #입력받은 소수를 리스트로 저장

for i in prime_list: # 리스트 하나씩 검사
  if isprime(i): # 소수면?
    count += 1 # +1
print(count)
