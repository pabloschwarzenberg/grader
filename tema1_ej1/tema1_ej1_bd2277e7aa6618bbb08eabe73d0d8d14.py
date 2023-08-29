#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

#Solicitar al usuario un número "N"
numero = int(input("Ingrese un número N: "))

#Calcular la suma de los N primeros números naturales 
resultado = suma_n_primeros_numeros(numero)

#Imprimir el resultado
print("La suma de los", numero, "primeros números naturales es:", resultado)
