#Ordenar tres números
#Definir la funcion oreden_numeros
def orden_numeros(n1,n2,n3):
 #Crear una lista con los numeros ingresados
  numeros=[n1,n2,n3]
#Ordenar la lista de mayor a menor
  numeros.sort()
 #Separar los numeros por una coma 
  numeros_ordenados=', '.join(str(n) for n in numeros)
  return numeros_ordenados

#Pedir al usuario el valor de los numeros
n1= int(input("Ingrese el valor del numero 1: "))
n2= int(input("Ingrese el valor del numero 2: "))
n3= int(input("Ingrese el valor del numero 3: "))

numeros_ordenados=orden_numeros(n1,n2,n3)
print("Los numeros ordenados de mayor a menor son: ",numeros_ordenados)

