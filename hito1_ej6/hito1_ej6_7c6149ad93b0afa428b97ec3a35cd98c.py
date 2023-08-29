#Ordenar tres números
lista=list()
for a in range(3):
    a=int(input("Ingrese un número:"))
    lista.append(a)
lista.sort()
m=""
for b in range(3):
    if b<2:
        m=m+str(lista[b])+","
    if b==2:
        m=m+str(lista[b])
print(m)