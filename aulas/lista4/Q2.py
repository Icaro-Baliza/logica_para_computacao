N=int(input())
U=list(map(float, input().split()))
V=list(map(float, input().split()))
D=list(map(float, input().split()))
P=[]
i=0
while i<=N-1:
    x=U[i]+V[i]
    P.append(x)
    i+=1
if D==P:
    print("OK")
else:
    print("NOPE :(")
