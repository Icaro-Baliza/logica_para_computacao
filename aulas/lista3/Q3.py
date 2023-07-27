p,s=input().split()
p=str(p)
s=int(s)
while p!="#" and s!=0:
    if s>=90:
        print(p,"Alta")
    else:
        print(p,"Internar")
    p,s=input().split()
    p=str(p)
    s=int(s)

