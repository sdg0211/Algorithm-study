import sys

input = sys.stdin.readline

N = int(input().rstrip())
stack = []

for i in range(N):
    s = input().rstrip()
    
    match s:
        case "top":
            if not len(stack): #len is 0
                print(-1)
            else:
                print(stack[-1])
        case "size":
            print(len(stack))
        case "empty":
            if not len(stack): #len is 0
                print(1)
            else:
                print(0)
        case "pop":
            if not len(stack): #len is 0
                print(-1)
            else:
                print(stack.pop())
        case _:
            x = int(s[5:])
            stack.append(x)
            
           
