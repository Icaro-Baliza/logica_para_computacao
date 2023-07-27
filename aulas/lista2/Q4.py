d=int(input())
l=d//3  
t=d%3
c=l
v=l
if t==2:
    c=l+1
    v=l+1
if t==1:
    c=l+1
print('Chapeuzinho Vermelho',c,'\nVovozinha',v,'\nLobo Mau',l)