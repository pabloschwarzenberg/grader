#Factores Primos
valor=int(input('ingresa valor'))
i=1
lista=[]
while i<valor:
    if valor%i==0:
        if i!=1:
            lista.append(i)
    i=i+1
j=0
i=1
c=0
while j<len(lista):
    if lista[j]%i==0:
        c=c+1
        i=i+1
        if c>2:
            lista[j].pop()
    j=j+1
lista=list(map(str,lista))
res=''.join(lista)
print(res)