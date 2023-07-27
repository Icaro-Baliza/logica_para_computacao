Q, C, O=input().split()
Q=int(Q)
P=[]
for i in range(Q):
    pokemon, level =input().split()
    P.append({"p": pokemon,
             "l": int(level)})
if C=="N" and O=="D":
    for x in range(1, Q):
        i=Q-1
        while i>=1:
            if P[i]["p"]>P[i-1]["p"]:
                P[i],P[i-1]=P[i-1],P[i]
            i-=1
if C=="N" and O=="C":
    for x in range(1, Q):
        i=Q-1
        while i>=1:
            if P[i]["p"]<P[i-1]["p"]:
                P[i],P[i-1]=P[i-1],P[i]
            i-=1 
if C=="L" and O=="D":
    for x in range(1, Q):
        i=Q-1
        while i>=1:
            if P[i]["l"]>P[i-1]["l"]:
                P[i],P[i-1]=P[i-1],P[i]
            i-=1
if C=="L" and O=="C":
    for x in range(1, Q):
        i=Q-1
        while i>=1:
            if P[i]["l"]<P[i-1]["l"]:
                P[i],P[i-1]=P[i-1],P[i]
            i-=1
for z in P:
   print(z["p"], z["l"])        

