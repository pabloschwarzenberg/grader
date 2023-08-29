#Ordenar tres números
lista=[]
m=3
while m!=0:
    n=int(input("ingrese un numero"))
    lista.append(n)
    m-=1
    lista.sort()
print(lista)     