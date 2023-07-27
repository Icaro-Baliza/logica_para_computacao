n=int(input())
x=0
for i in range(n):
    l,c=input().split()
    l=int(l)
    c=int(c)
    if l>c:
        x=x+c
print(x)
