n = int(input())
li = map(int, input().split())
target = int(input())

cnt=0

for j in li:
    if j == target:
        cnt+=1
        
print(cnt)
    