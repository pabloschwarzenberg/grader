# Sumar números naturales usando fórmula de Gaus 
num = eval(input("Por favor ingrese un numero: "))
suma = num * (num + 1) /2
print(suma)


# Sumar usando un ciclo
suma_ciclo = 0 
for i in range(1, num + 1):
    suma_ciclo += 1
print(suma_ciclo)


# Usando la función sum:1
sum = sum(range(1, num + 1))
print(sum)
      