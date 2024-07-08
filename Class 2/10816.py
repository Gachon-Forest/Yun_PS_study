'''
Date: 2024.07.08
No: 10816
Tier: Sliver 4
Name: 숫자 카드 2
Language: Python 3
'''
from collections import Counter
import sys 

n = int(sys.stdin.readline())
nlist = list(map(int, input().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, input().split()))

count = Counter(nlist)
print(count)
#원소 : 갯수 꼴의 딕셔너리로 반환해줌

for i in range(len(mlist)):
    if mlist[i] in count:
        print(count[mlist[i]], end=' ')
    else:
        print(0, end=' ')