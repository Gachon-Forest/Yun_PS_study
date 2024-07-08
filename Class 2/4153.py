'''
Date: 2024.07.07
No: 4153
Tier: Bronze 3
Name: 직각삼각형
Language: Python 3
'''

#0 = a, 1 = b, 2 = c
while(True):
  num = sorted(list(map(int, input().split(" "))))
  # sorted를 쓴 이유 -> 피타고라스의 정리는 빗변의 길이가 c인 직각 삼각형에서 성립함.
  # 이때, a 또는 b가 c보다 크거나 같은 경우 삼각형이 성립하지 않으므로, c를 가장 큰 값으로 설정하기 위함
  # 따로 max 함수를 이용해서 뽑아도 되지만, sorted를 통해 리스트로 선언하는게 편하다고 생각함.
  if(sum(num) == 0):
    break
  print("right" if num[0] ** 2 + num[1] ** 2 == num[2] ** 2 else "wrong")
  
