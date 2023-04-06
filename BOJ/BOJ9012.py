import sys

input = sys.stdin.readline

T = int(input().rstrip()) #number of repeating 

for i in range(T):
    stack = []
    flag = 0 #default not finished
    s = input().rstrip()
    
    for j in s:
        if j == '(':
            stack.append(j)
        else: #j == ')'
            if len(stack) == 0: #stack is empty
                flag = 1 # already finished
                print("NO")
                break 
            else:
                stack.pop()
    
    if flag == 0: #not finished
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
