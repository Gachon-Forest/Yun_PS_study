'''
Date: 2024.07.07
No: 1259
Tier: Bronze 1
Name: 펠린드롬 수
Language: Python 3
'''

# 기억하자. 파이썬은 문자열 처리의 신이다.

def reverse(a): # 문자를 뒤집는 함수
  temp = ""
  for i in range(len(a) -1 , -1, -1): #글자의 마지막 인덱스 부터, 첫번쨰 인덱스 까지 역순으로. 
    temp += a[i]
  return temp


while(True):
  a = input() #문자열로 입력받음.
  if a == "0": # 0 입력 받으면 종료
    break
  else: 
    print("yes"if a == reverse(a) else "no") # 뒤집은거랑 a랑 같으면 yes, 아니면 no



