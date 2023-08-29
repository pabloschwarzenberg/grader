#Suma de los N primeros números
def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo.")
else:
    resultado = suma_n_primeros_numeros(numero)
    print(resultado)     