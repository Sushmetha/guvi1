X=int(input())
Y=list(map(int,input().split()))
Z=[]
for i in Y:
    if(Y.count(i)>1):
        Z.append(i)
E=set(Z)
if len(E)==0:
    print("unique")
else:
    print(*E)
