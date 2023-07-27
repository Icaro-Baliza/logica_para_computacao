a,b=input().split()
a=int(a)
b=int(b)
p=0
x=0
while a<b+1:
    for i in range(1,b+1):
        if a%i==0:
            x+=1
        if x>2:
            break
    if x<=2:
        p+=1
    a+=1
    x=0
print(p)

    