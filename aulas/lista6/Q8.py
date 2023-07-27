N,M=map(int, input().split())
c=[]
for i in range(N):
    lista=list(map(int, input().split()))
    for elemento in lista:
        c.append(elemento)
c=sorted(c)
Q=int(input())
horas=list(map(int, input().split()))
for hora in horas:
    esq = 0
    dir = len(c)-1
    while dir>esq:
        meio=(dir+esq)//2
        if hora<c[meio]:
            dir=meio
        else:
            esq=meio+1
    if c[dir]<=hora:
        print(dir+1)
    else:
        print(dir)
 

