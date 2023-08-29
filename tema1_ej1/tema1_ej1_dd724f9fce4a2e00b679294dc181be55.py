#Suma de N primeros numeros
def suma_de_n(n):
    suma = n * (n + 1) / 2
    return suma

#Programa
#Entrada
n = int(input("Ingrese un numero natural: "))
#Verificar
if n < 0:
    print("El numero debe ser positivo")
else:
    resultado = suma_de_n(n)
    print("La suma de los {n} primeros numeros naturales es: " + str(resultado))      