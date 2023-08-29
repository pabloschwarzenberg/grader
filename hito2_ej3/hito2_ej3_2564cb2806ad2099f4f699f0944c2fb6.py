s=input("string: ")
s=s.lower()
n=int(input("numero:"))
b=[]
am=[]
c=['ninguna']
for i in range(0, len(s)-(n-1)):
    ar=s[i:i+3]
    b.append(ar)
for i in range(0, len(s)-(n-1)):
    if b.count(s[i:i+n])==1:
        
        am.append(s[i:i+n])

if len(am)==0:
    print(c)
else:
    print(am)     