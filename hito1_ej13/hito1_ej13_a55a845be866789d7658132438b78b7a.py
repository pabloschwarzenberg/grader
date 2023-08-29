#Factores Primos
def factorizar_primos(numero):
    # Inicializamos una lista vacía para almacenar los factores primos
    factores_primos = []

    # Iteramos desde 2 hasta la raíz cuadrada del número, buscando factores primos
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            # Si encontramos un factor primo, lo agregamos a la lista
            factores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1

    # Si el número restante es mayor que 1, también es un factor primo
    if numero > 1:
        factores_primos.append(numero)

    return factores_primos

# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Obtenemos la descomposición en factores primos del número
factores = factorizar_primos(numero)

# Imprimimos cada factor primo en una línea separada
print("La descomposición en factores primos de", numero, "es:")
for factor in factores:
    print(factor)
      