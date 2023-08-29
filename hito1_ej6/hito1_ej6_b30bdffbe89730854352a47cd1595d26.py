#Ordenar tres números
num1=int(input("ingrese un número entero: "))
num2=int(input("ingrese otro número entero: "))
num3=int(input("ingrese otro número entero: "))
#se agregan los números a una lista
lista=num1,num2,num3
#se ordenan con sorted
listaOrdenada=sorted(lista)
#se imprime el mensaje, con la lista ordenada
print("sus números ordenados de menor a mayor son: ",listaOrdenada)    