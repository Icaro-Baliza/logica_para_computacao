N=int(input())
V=[]
for i in range(N):
    data=int(input())
    V.append(data)
for l in range(1, N):
    i = N-1
    while i>=1:
        if V[i]<V[i-1]:
            V[i],V[i-1]=V[i-1],V[i]
        i-=1
for x in V:
   print(x)
