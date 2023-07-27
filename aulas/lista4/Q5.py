N=int(input())
E=list(map(int,input().split()))
Verdadeiras=[n for n in E if n<8]
Ordem=[]
for i in range(8):
    if (i) in (Verdadeiras):
        Ordem.append(i)
print(*Ordem)
if len(Ordem)==7:
    print("Saia Shenlong e realize o meu desejo")
else:
    print("Nao encontramos todas")