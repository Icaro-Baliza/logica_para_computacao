N=int(input())
P=list(map(int, input().split()))
C=int(input())
i=0
soma=0
while i<N:
    if P[i]==C:
        P[i]*=(-1)
    soma+=P[i]
    i+=1
print(soma)


