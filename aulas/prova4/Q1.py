N=int(input())
area=[]
coor=[]
total=0
for i in range(N):
    lista=list(map(int, input().split()))
    area.append(lista)
C=int(input())
for n in range(C):
    listo=list(map(int, input().split()))
    coor.append(listo)
for l in range(C):
    total+=area[coor[l][0]][coor[l][1]]
print(total)

    



