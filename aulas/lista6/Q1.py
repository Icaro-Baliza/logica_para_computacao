n=int(input())
N=list(map(int, input().split()))
for l in range(8):
    i=n-1
    while i>=1:
        if N[i]<N[i-1]:
            N[i],N[i-1]=N[i-1],N[i]
        i-=1
for x in range(8):
        print(N[x], end=" ")