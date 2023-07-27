N=int(input())
V=int(input())
t=N*V
t=int(t)
if t>=7500:
    print("Vara de Iridio")
elif 1800<=t<7500:
    print("Vara de Fibra de Vidro")
elif 500<=t<1800:
    print("Vara de Bambu")
elif 500>t:
    print("Paciencia Firmino!")

