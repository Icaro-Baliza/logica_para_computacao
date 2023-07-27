l1,p1=input().split()
l1=int(l1)
p1=int(p1)
l2,p2=input().split()
l2=int(l2)
p2=int(p2)
l3,p3=input().split()
l3=int(l3)
p3=int(p3)
L=int(l1+l2+l3)
P=int(p1+p2+p3)
if L>P:
    print('Lucas')
if P>L:
    print('Pedro')
if P==L:
    print('Empate')
        
