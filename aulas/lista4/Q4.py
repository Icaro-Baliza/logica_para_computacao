S,N=input().split()
S=int(S)
N=int(N)
LP=[]
Pedras=[0]*N
i=0
m=0
for n in range(S):
    Pulos=int(input())
    LP.append(Pulos)
while m<S:
    while i<N:
        if i%LP[m]==0:
            Pedras[i]=1
        i+=1
    m+=1
    i=0
print(*Pedras)


    

        
    
