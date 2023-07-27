N=int(input())
S=[]
for i in range(N):
    planeta, grau = map(int, input().split())
    S.append({"planeta": planeta,"urgência": grau})
for l in range(1, N):
    i = N-1
    while i>=1:
        if S[i]["urgência"]>S[i-1]["urgência"]:
            S[i],S[i-1]=S[i-1],S[i]
        i-=1
for x in S:
   print(x["planeta"], x["urgência"])
