#Factores Primos
n = int (input("Ingrese el número al que calcular el factorial: "))
# Calculo
# Condiciones iniciales
# Iterador
i = n
# Producto
factorial = 1
# Ciclo principal
while i > 1:
    factorial *= i
    i -= 1

# SAlida
print("El factorial es" , factorial)