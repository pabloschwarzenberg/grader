#Suma de los N primeros números
def suma_numeros(n):
    suma = (n * (n + 1)) / 2
    return suma

n= int(input("Ingrese un número: "))
resultado= suma_numeros(n)
print(resultado)