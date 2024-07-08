'''
Date: 2024.07.07
No: 30802
Tier: Bronze 3
Name: 웰컴 키트
Language: Python 3 
'''

T = int(input()) #테스트 케이스
L = list(map(int, input().split())) # 티셔츠 사이즈
P = list(map(int, input().split())) # P[0] = 티셔츠 묶음 수, P[1] = 펜의 묶음 수
T_set = 0


for i in L:
  T_set += i//P[0] if i % P[0] == 0 else i//P[0] + 1 
  # 티셔츠 주문 수량 != 묶음수 -> 주문 수량 // 묶음수 + 1 (옷의 수량이 남아도 되기 때문에)
  # 티셔츠 주문 수량 == 묶음수 -> 주문 수량 // 묶음수(딱 맞게 주문할 수 있으므로)
  # 모든 티셔츠 사이즈 별로 계산 후 각각의 수량을 T_set 변수에 저장

print(T_set)
print(T//P[1], T%P[1]) #전체 사람을 펜의 묶음 수로 나눈 몫과 나머지 

