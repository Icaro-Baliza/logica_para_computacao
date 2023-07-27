N,M=map(int,input().split())
matrizA=[]
naves=0
for i in range(N):
    lista=list(map(int, input().split()))
    matrizA.append(lista)
for c in range(M):
    A,B=map(int,input().split())
    l=A
    while l>=0:
        if matrizA[l][B]==1:
            naves+=1
            matrizA[l][B]=0
            break
        l-=1
print(naves)

