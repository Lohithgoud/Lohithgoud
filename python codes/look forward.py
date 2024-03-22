l=list(map(int,input().split()))
b=[]

for i in range(len(l)-1):
    if l[i]>max(l[i+1:]):
        b.append(l[i])
b.append(l[-1])
print(b)
