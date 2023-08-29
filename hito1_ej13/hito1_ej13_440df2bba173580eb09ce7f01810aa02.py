#Factores Primos
numero = int(input())

# Dividir el número entre 2 hasta que ya no sea divisible por 2
while numero % 2 == 0:
    print(2)
    numero = numero // 2

# Buscar factores primos impares desde 3 hasta la raíz cuadrada del número
i = 3
while i * i <= numero:
    while numero % i == 0:
        print(i)
        numero = numero // i
    i = i + 2

# Si el número restante es mayor que 2, es un factor primo
if numero > 2:
    print(numero)
            
      
      