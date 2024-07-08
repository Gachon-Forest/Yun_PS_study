'''
Date: 2024.07.08
No: 10828
Tier: Sliver 4
Name: 스택
Language: Python 3
'''

import sys

stack = []
n = int(sys.stdin.readline())
for i in range(n):
    c = list(sys.stdin.readline().split())
    if len(c) == 2:
        stack.append(int(c[1]))
    elif c[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif c[0] == "size":
        print(len(stack))

    elif c[0] == "empty":
        print(1 if len(stack) == 0 else 0)

    else: # top
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

