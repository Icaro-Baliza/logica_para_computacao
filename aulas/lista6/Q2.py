P=int(input())
IH=list(map(int, input().split()))
MH=list(map(int, input().split()))
n=0
for l in range(1, P):
    i = P-1
    while i>=1:
        if IH[i]>IH[i-1]:
            IH[i],IH[i-1]=IH[i-1],IH[i]
        if MH[i]<MH[i-1]:
            MH[i],MH[i-1]=MH[i-1],MH[i]
        i-=1
    print(IH[n],"",MH[n])
    n+=1
print(IH[P-1],"",MH[P-1])
