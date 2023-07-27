pf=int(input())
lc=int(10)
matriz=[]
ver=0
for i in range(lc):
    lista=list(map(int, input().split()))
    matriz.append(lista)
for n in range(lc):
    if pf in matriz[n]:
        ver=1
        break
if ver==1:
    print("sim")
else:
    print("nao")
    