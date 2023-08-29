adn=str(input())
n=int(input())
i=0
j=n
listasa=[]
resultado=[]
while j<len(adn)+1:
    x=adn[i:j]
    listasa.append(x)
    i=i+1
    j=j+1
z=0
while z <len(listasa):
    if listasa.count(listasa[z])>1:
        resultado.append("ninguna")
    if listasa.count(listasa[z])==1:
        resultado.append(listasa[z])
    z=z+1
q=0
for a in resultado:
    if a!="ninguna":
        print(a)
    else:
        q+=1
if q==len(resultado):
    print("ninguna")



