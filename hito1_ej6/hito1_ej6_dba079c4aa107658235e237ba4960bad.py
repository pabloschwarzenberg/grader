#Ordenar tres números
#Recopilacion de datos
n1 = int(input("Ingresa el 1er digito: "))
n2 = int(input("Ingresa el 2do digito: "))
n3 = int(input("Ingresa el 3er digito: "))

#Orden de numeros de mayor a menor
def ordenN(n1, n2, n3):
    numeros = [n1, n2, n3]
    numeros.sort()
    fin = ", ".join(str(n)for n in numeros)
    return fin

#Imprimir numeros ingresados por el usuario en orden
num_ordenados = ordenN(n1, n2, n3)
print("Los numeros ingresados ordenados de menor a mayor son los siguientes: ",num_ordenados)
      