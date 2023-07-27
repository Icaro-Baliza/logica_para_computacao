N,M=map(int,input().split())
matrizA=[]
ovos=0
for i in range(N):
    lista=list(map(int, input().split()))
    matrizA.append(lista)
for l in range(N):
    for c in range(M):
        if l%2==0:
            ovos+=matrizA[l][c]
        else:
            ovos+=matrizA[N-l-1][M-c-1]
        if ovos<0:
            ovos=0
print(ovos)
            

