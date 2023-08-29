r=input()
lista=[]
mult=[2,3,4,5,6,7,2,3,4,5,6,7,2,3,4,5,6,7]
for i in r:
    lista.append(i)
print(lista)
l=lista[::-1]
i=0
suma=0
while i<len(l):
    n=int(l[i])*mult[i]
    suma+=n
    i+=1
print(suma)
resto=suma%11
print(resto)
r=11-resto
print(r)
if r==11:
    print("dv=0")
if r==10:
    print("dv=k")
else:
    print("dv=",r)
