N=int(input())
U=list(map(int, input().split()))
I=[n for n in U if n%2==1]
P=[n for n in U if n%2==0]
print(*P)
print(*I)

