t=float(input())
h=t//3600
m=(t%3600)//60
s=(t%3600)%60
h=int(h)
m=int(m)
s=int(s)
print(h,'h ',m,'m ',s,'s',sep='')
