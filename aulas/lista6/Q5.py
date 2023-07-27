N=int(input())
v=list(map(int, input().split()))
p=list(map(int, input().split()))
for n in p:
    esq=0
    dir=N-1
    if n == 0:
        break
    while esq <= dir:
        meio = (dir + esq) // 2
        if v[meio] == n:
            break
        elif n < v[meio]:
            dir = meio - 1
        else:
            esq = meio + 1
    if v[meio] == n:
        print(meio)
    else:
        print("Nao foi visitado ainda.")

