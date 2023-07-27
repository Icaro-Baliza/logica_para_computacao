N,M=map(int,input().split())
codigo=[]
perfeito=[[0]*M for l in range(N)]
for i in range(N):
    lista=list(map(int, input().split()))
    codigo.append(lista)
A=int(input())
for n in range(A):
    i,j=map(int, input().split())
    codigo[i-1][j-1]=0
if codigo==perfeito:
    print("HASTA LA VISTA BABY")
else:
    print("ILL BE BACK")