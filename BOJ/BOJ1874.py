import sys

input = sys.stdin.readline
n = int(input().rstrip())

last_num = 0
stack = []

flag = 0 #flag ...

answer = ''

for i in range(n):
    x = int(input().rstrip())
    
    if last_num < x: #last_num update
        #push inquired
        for j in range(x-last_num):
            stack.append(j+last_num+1)
            answer += '+'
        last_num = stack[-1]
        answer += '-'
        stack.pop()
    else: #last_num doesn't same with any next x
        # pop inquired
        if stack[-1] == x:
            answer += '-'
            stack.pop()
        else: #cannot be a stack sequence 
            flag = 1
            print("NO")
            break
            
if flag == 0: #stack sequence
    for i in answer:
        print(i)
