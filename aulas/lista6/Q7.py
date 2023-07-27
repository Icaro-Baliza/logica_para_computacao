N=int(input())
p=list(input().split())
x=int(input())
t=list(input().split())
d=[]
total=0
anterior=0
for i in range(N):
    lista=list(map(int, input().split()))
    d.append(lista)
for planeta in t:
    esq=0
    dir=N-1
    while esq <= dir:
        meio = (dir + esq) // 2
        if p[meio] == planeta:
            break
        elif planeta < p[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if p[meio] == planeta:
        total+=d[anterior][meio]
        anterior=meio
print(total)