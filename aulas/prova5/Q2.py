N,M=map(int, input().split())
n=list(map(int, input().split()))
m=list(map(int, input().split()))
soma=0
for b in m:
    esq=0
    dir=N-1
    while esq <= dir:
        meio = (dir + esq) // 2
        if n[meio] == b:
            break
        elif b < n[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if n[meio] == b:
        soma+=1
print(soma)
    
