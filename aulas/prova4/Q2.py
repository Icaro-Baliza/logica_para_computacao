tabuleiro=[]
d=1
e=1
c=1
b=1
total=0
for i in range(8):
    lista=list(map(int, input().split()))
    tabuleiro.append(lista)
x,y=map(int, input().split())
while x+d!=8 and tabuleiro[x+d][y]!=1:
    if tabuleiro[x+d][y]==2:
        total+=1
        break
    d+=1
while x-e!=-1 and tabuleiro[x-e][y]!=1:
    if tabuleiro[x+e][y]==2:
        total+=1
        break
    e+=1
while x+b!=8 and tabuleiro[x][y+b]!=1:
    if tabuleiro[x][y+b]==2:
        total+=1
        break
    b+=1
while x-c!=-1 and tabuleiro[x][y-c]!=1:
    if tabuleiro[x][y-c]==2:
        total+=1
        break
    c+=1
print(total)
    
