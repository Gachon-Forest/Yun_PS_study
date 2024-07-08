'''
Date: 2024.07.08
No: 11866
Tier: Sliver 5
Name: 요세푸스 문제 0
Language: Python 3
'''

# 맨 처음 문제볼땐 어지러웠는데, 원이라는 내용을 강조한 이유가 있었다.
# 간단하게 말해서, k번째 전까지는 리스트 맨 앞의 값을 맨 뒤로 옮기는 작업을 하다가, k번째때 맨 앞의 값을 빼서 따로 저장하면 되는 것이였다.
# 구현 아이디어만 있으면 충분히 풀 수 있는 문제다. 

n, k = map(int, input().split())
p = []
arr = [i for i in range(1, n+1)]
while(len(arr) != 0):
    for i in range(k - 1):
        temp = arr.pop(0) 
        arr.append(temp)
    p.append(arr.pop(0))


#출력 형식이 이따구인건 진짜 사람 놀리려고 한게 분명하다.. ㅡㅡ 

print("<", end = "")
for i in range(len(p)-1):
    print(p[i], end = ", ")
print(str(p[-1]) + ">")