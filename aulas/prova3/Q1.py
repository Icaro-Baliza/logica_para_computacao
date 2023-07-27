N=int(input())
S=list(map(int, input().split()))
i=0
soma=0
while i<N:
    soma+=S[i]
    i+=1
x=soma/2
n=0
div=0
while n<N:
    div+=S[n]
    if div==x:
        print(n+1)
        break
    n+=1