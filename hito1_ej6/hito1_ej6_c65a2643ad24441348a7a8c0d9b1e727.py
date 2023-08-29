#Ordenar tres números
lista=[]
t= True
while t:
    n=input('ingresa numero ')
    lista.append(n)
    if len(lista) != 3:
        t=True
    if len(lista) == 3:
        break

lista.sort()
t=','.join(lista)
print(t)



