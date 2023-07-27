a,d,p=input().split()
a=int(a)
d=int(d)
p=int(p)
t=a+d+p #total de poder
v=(t*100)//110 #valor da porcentagem
if 80<=v<=100:
    print('Seu pokemon e uma maravilha')
elif 67<=v<=79:
    print('Seu pokemon certamente me chamou atencao')
elif 51<=v<=66:
    print('Seu pokemon esta acima da media')
elif 0<=v<=50:
    print('Seu pokemon nao fara progresso em batalhas')
else:
    print('Hum, parece que houve um erro')