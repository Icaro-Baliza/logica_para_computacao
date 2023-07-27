N,M=map(int,input().split())
matrizA=[]
matrizB=[]
for i in range(N):
    lista=list(map(int, input().split()))
    matrizA.append(lista)
for n in range(N):
    lista=list(map(int, input().split()))
    matrizB.append(lista)
matrizC=matrizA
for t in range(N):
    for c in range(M):
        matrizC[t][c]-=matrizB[t][c]
        print(matrizC[t][c], end=" ")
    print()
    



