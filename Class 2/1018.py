'''
Date: 2024.07.08
No: 1018
Tier: Sliver 4
Name: 체스판 다시 칠하기
Language: Python 3
'''
# 진짜 잘 모르겠어서, 문제 해석만 찾아서 봄.
# 코드는 해석 보고 구현 해본거
# 2차원 리스트 기반 좌표 문제는 연습이 필요할 듯.

n, m = map(int, input().split())
l = []
result = []
for _ in range(n):
    l.append(input())

for x in range(n-7):
    for y in range(m-7):
        startWhite = 0 #시작점(왼쪽 위 꼭짓점)이 흰색일 때 
        startBlack = 0

        for r in range(x, x+8):
            for c in range(y, y+8):
                if (r+c) % 2 == 0: # r + c가 짝수이면서
                    if l[r][c] != "B": #시작점(왼쪽 위 꼭짓점)이 검은색일 때, [r][c]가 하얀색이면
                        startBlack += 1
                    if l[r][c] != "W": #시작점(왼쪽 위 꼭짓점)이 하얀색일 때, [r][c]가 검은색이면
                        startWhite += 1
                else: # r + c 가 홀수 이면서
                    if l[r][c] != "W": #시작점(왼쪽 위 꼭짓점)이 검은색일 때, [r][c]가 검은색이면
                        startBlack += 1
                    if l[r][c] != "B": #시작점(왼쪽 위 꼭짓점)이 하얀색일 때, [r][c]가 하얀색이면
                        startWhite += 1

        # 결국 우리가 생각해야 하는 사례는 두가지(시작점이 검정인지, 하양인지)밖에 없으므로
        # 모든 범위에서 두가지 경우의 수에 따른 가중치를 계산하여 그 중 최소 값을 고르면 되는 것.
        result.append(startBlack)
        result.append(startWhite)

print(min(result))
