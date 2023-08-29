s=str(input())
n=int(input())
c=[]
d=[]
for letter in s:
    c.append(letter)
for i in range(0,int(len(s))):
    if len(c[i:i+n])==n:
        d.append(''.join(c[i:i+n]))
f=[]
while len(d)>0:
    j=d.pop(0)
    if str(j) in d != -1:
        while str(j) in d != -1:
            d.remove(j)
    else:
        f.append(j)
if len(f)>0:
    for elem in f:
        print(elem)
else:
    print("ninguna")