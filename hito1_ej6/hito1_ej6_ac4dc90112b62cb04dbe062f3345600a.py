#Ordenar tres números
x=0
lista=[]
while x<3:
    n=int(input("Ingrese un numero "))
    lista.append(n)
    x=x+1
lista.sort()
print(lista)    