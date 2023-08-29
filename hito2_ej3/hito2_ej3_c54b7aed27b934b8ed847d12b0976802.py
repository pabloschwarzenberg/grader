cad=input()
num=int(input())
i=0
l=[]
l2=[]
resp=[]
while i < len(cad):
    j=0
    while i + j < len(cad):
        l.append(cad[i:j + i + 1])
        j=j+1
    i=i+1
for n in l:
    if len(n)==num and l.count(n)==1:
        l2.append(n)
if len(l2)<1:
    print(['ninguna'])
else:
    print("%s"%(l2))