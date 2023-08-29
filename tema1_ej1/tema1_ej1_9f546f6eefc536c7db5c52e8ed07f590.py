#Suma de los N primeros números
def suma_de_numeros_naturales(n):
    suma = n * (n + 1) // 2
    return suma

n = int(input("Ingrese un número que desee sumar: "))

resultado = suma_de_numeros_naturales(n)


print("la suma de los", n, "primeros números naturales es:", resultado)       