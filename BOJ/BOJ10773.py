import sys

input = sys.stdin.readline
K = int(input().rstrip())

stack = []

for i in range(K):
    n = int(input().rstrip())
    
    if not n:
        stack.pop()
    else:
        stack.append(n)
        
print(sum(stack))
