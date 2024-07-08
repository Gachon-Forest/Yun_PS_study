'''
Date: 2024.07.07
No: 9012
Tier: Sliver 4
Name: 괄호
Language: Python 3
'''

for i in range(int(input())): #입력받은 숫자만큼 반복
    ps = input() # 문자열 입력
    psl = []
    for p in ps: # 문자열 하나씩 순회
        if p == "(": # 해당 문자열에 열린 괄호가 있으면
            psl.append("(") # psl 리스트에 열린 괄호를 넣음
        else: # 해당 문자열에 닫힌 괄호가 있으면
            if len(psl)!= 0: #만약 psl의 길이가 0이 아니라면 
                psl.pop() #앞에 있는 열린 괄호를 제거함
            else: #psl의 길이가 0이라면 -> 열린 괄호보다 닫힌 괄호가 먼저 나오거나, 많이 나오면
                psl.append(")") # 닫힌 괄호를 psl에 넣고 
                break # 종료

    if len(psl)!= 0: #psl의 길이가 0이 아니면
        print("NO") # No
    else:
        print("YES")