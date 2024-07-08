'''
Date: 2024.07.08
No: 10845
Tier: Sliver 4
Name: 큐
Language: Python 3
'''

import sys

queue = []
n = int(sys.stdin.readline())
for i in range(n):
    c = list(sys.stdin.readline().split())
    if len(c) == 2:
        queue.append(int(c[1]))
    elif c[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif c[0] == "size":
        print(len(queue))

    elif c[0] == "empty":
        print(1 if len(queue) == 0 else 0)

    elif c[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    else: # back
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

