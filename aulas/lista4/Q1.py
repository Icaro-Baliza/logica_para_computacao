
caixas=int(input())
num=list(map(int, input().split()))
c=int(input())
for i in num:
    if(i==c):
        break
if i==c:
    print(c)
else:
    print("-1")


