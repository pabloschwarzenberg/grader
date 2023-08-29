#Ordenar 3 numeros de mayor a menor
def ordenar_num(a, b, c):
    numeros = [a, b, c]
    numeros.sort()
    return numeros

#Programa
#Entrada
num = []
n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))
n3 = int(input("Ingrese numero 3: "))
#Proceso
num = ordenar_num(n1, n2, n3)
#Salida
print("Los numeros ordenados son: " + str(num[0])+", " + str(num[1])+", " + str(num[2]))