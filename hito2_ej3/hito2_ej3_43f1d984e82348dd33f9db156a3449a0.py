string=input()
n=int(input())
b=[]
c=0
if (len(string))%n!=0:
    print("ninguna")
else:
    while n<=len(string):
        b.append(string[c:n])
        c+=1
        n+=1
d=0
while d<len(b):
    e=b.count(b[d])
    f=b[d]
    if e>1:
        while e>0:
            b.remove(f)
            e-=1
    d+=1
print(b)