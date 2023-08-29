def suma_n_primeros_numeros(n):
    suma = n * (n + 1) // 2
    return suma

#Ingrese un número
numero = int(input("Ingresa un número: "))

# Calculamos la suma de los primeros números naturales
resultado = suma_n_primeros_numeros(numero)

#El resultado
print("La suma de los", numero, "primeros números naturales es:", resultado)
      