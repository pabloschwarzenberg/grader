# Sumar números naturales usando fórmula de Gaus 
n = eval(input("Ingrese un numero: "))
suma = n * (n + 1) /2
print(suma)


# Sumar usando un ciclo
suma_ciclo = 0 
for i in range(1, n + 1):
    suma_ciclo += 1
print(suma_ciclo)


# Usando la función sum:1
sum = sum(range(1, n + 1))
print(sum)