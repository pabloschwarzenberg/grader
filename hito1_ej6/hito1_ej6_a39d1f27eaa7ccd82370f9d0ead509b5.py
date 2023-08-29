#Ordenar tres números
numero1=int(input("dame un numero:"))
numero2=int(input("dame un numero otra ves:"))
numero3=int(input("dame un numero por ultima ves:"))

lista=[]
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.sort()
print(lista[0],",",lista[1],",",lista[2])