N,Q=list(map(int, input().split()))
S=[]
for i in range(Q):
    NQI, IDQI = map(int, input().split())
    S.append({"NQI": NQI,"IDQI": IDQI})
for l in range(Q-1):
    b = Q-1
    while b>=1:
        if S[b]["NQI"]>S[b-1]["NQI"]:
            S[b],S[b-1]=S[b-1],S[b]
        if (S[b]["NQI"]==S[b-1]["NQI"] and S[b]["IDQI"]<S[b-1]["IDQI"]):
            S[b],S[b-1]=S[b-1],S[b]
        b-=1
C=int(input())
V=[]
for a in range(C):
    NCI, ICQI = map(int, input().split())
    V.append({"NCI": NCI,"IDCI": ICQI})
for pessoa in V:   
    esq=0
    dir=Q-1
    while esq <= dir:
        meio = (dir + esq) // 2
        if S[meio]["NQI"] == pessoa["NCI"] and S[meio]["IDQI"]==pessoa['IDCI']:
            break
        elif pessoa["NCI"] > S[meio]["NQI"] or (S[meio]["NQI"] == pessoa["NCI"] and S[meio]["IDQI"]>pessoa['IDCI']):
            dir = meio - 1
        else:
            esq = meio + 1
    if meio<N:
        print("Sim")
    else:
        print("Nao")

