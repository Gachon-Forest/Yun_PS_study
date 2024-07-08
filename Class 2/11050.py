'''
Date: 2024.07.07
No: 11050
Tier: Bronze 1
Name: 이항계수
Language: Python 3
'''

# 사실.. 이전에 알고리즘 공부하면서 Divide and Conquer를 적용한 조합 알고리즘을 미리 작성한 바 있다.
# 그거 들고온거다.. ><

MAX_n = 1000 # n's maximum size in nCr
MAX_r = 1000 # r's maximum size in nCr


val = [[-1 for i in range(MAX_n + 1)] for j in range(MAX_r + 1)] 

#Once we Calculate nCr, we save it in "val" list. (= Memoization)
#If we calculate nCr since we saved, we return val[n][r] instead of calculate it again.


def comb(n, r):
  if n == r or r == 0: #nC0 = 1, nCn == 1
    return 1

  if r == 1: #nC1 = n
    return n

  if val[n][r] != -1: #if we save nCr before
    return val[n][r] #return val[n][r] instead of calculate it.
  else:
    val[n][r] = comb(n-1,r)+comb(n-1,r-1) #we save nCr in "val" list
    return val[n][r] # And, return it.


n, k = map(int, input().split())
print(comb(n, k))
 