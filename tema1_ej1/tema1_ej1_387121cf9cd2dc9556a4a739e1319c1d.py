#Suma de los N primeros números
def suma_num_naturales(n):
    suma = n * (n+1) // 2
    return suma
    
num = int(input("Ingrese el número N: "))
resultado = suma_num_naturales(num)
print("La suma de los primeros", num, "números naturales es:", resultado)