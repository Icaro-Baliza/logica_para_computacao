matrizA=[]
for i in range(10):
    lista=list(input().split())
    matrizA.append(lista)
for l in range(10):
    for c in range(10):
        if matrizA[l][c]=="t":
            v=[]
            for dl in range(-1,2):
                for dc in range(-1,2):
                    if (l+dl>=0 and l+dl<10 and c+dc>=0 and c+dc<10):
                        if (l+dl==l and c+dc!=c) or (l+dl!=l and c+dc==c):
                            v.append([l+dl,c+dc])
            for elemento in v:
                if matrizA[elemento[0]][elemento[1]]=="*":
                    matrizA[l][c]="p"
                    break
for t in range(10):
    for k in range(10):
        print(matrizA[t][k], end=" ")
    print()
                        







            

            

       


