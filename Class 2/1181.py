'''
Date: 2024.07.08
No: 1181
Tier: Sliver 5
Name: 단어정렬
Language: Python 3
'''


#파이썬 sort는 진짜 개 사기다.

N = int(input())
temp = []
for _ in range(N):
    temp.append(input())

word = list(set(temp)) #중복 제거를 위해 집합으로 바꾼 뒤, 다시 리스트로 바꿔주기
word.sort() # 알파벳 순으로 정렬
word.sort(key = len) # 길이 순으로 정렬
for i in word:
    print(i)