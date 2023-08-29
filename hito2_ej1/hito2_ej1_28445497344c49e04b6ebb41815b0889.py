base=input()
nueva=input()
lista=[]
a=0
for letra in nueva:
    lista.append(base[a:].find(letra))
    a=a+base[a:].find(letra)+1
for i in range(0,len(lista)):
    if lista[i]==-1:
        lista[i]=0
print(lista)
nuevalista=[]
for a in nueva:
    nuevalista.append(a)
print(nuevalista)
for i in range(0,len(nuevalista)):
    if lista[i]!=0:
        espacios=""
        for j in range(0,lista[i]):
            espacios=espacios+"_"
        nuevalista[i]=espacios+nuevalista[i]
print("".join(nuevalista))