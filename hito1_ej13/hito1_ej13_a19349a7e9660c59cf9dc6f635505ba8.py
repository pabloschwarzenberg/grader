#Factores Primos
def factorizar_numero(numero):
    # Inicializar la lista de factores primos
    factores_primos = []
    
    # Dividir el número por 2 hasta que ya no sea divisible
    while numero % 2 == 0:
        factores_primos.append(2)
        numero = numero // 2
    
    # Probar los siguientes números impares como factores primos
    # Empezando desde 3 hasta la raíz cuadrada del número
    for i in range(3, int(numero**0.5) + 1, 2):
        while numero % i == 0:
            factores_primos.append(i)
            numero = numero // i
    
    # Si el número es mayor a 2, entonces es primo
    if numero > 2:
        factores_primos.append(numero)
    
    # Imprimir cada factor primo en una línea separada
    for factor in factores_primos:
        print(factor)

# Pedir al usuario que ingrese un número entero
numero = int(input())

# Llamar a la función para factorizar el número ingresado
factorizar_numero(numero)
      