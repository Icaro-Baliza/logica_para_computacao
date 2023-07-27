t,d=input().split()
t=int(t)
d=int(d)
v,p=input().split()
v=int(v)
p=int(p)
pedagios=int(t/d) #numero de pedagios
valor=int(v*t) #valor do a pagar pela distancia percorrida
gasto=int(pedagios*p) #valor gasto nos pedagios
T=int(gasto+valor)
print(T)