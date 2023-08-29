#Factores Primos
  def descomposicion_factores_primos(numero):
    # Función para determinar si un número es primo
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Descomposición de factores primos
    factores_primos = []
    divisor = 2

    while divisor <= numero:
        if numero % divisor == 0:
            if es_primo(divisor):
                factores_primos.append(divisor)
                numero = numero // divisor
            else:
                divisor += 1
        else:
            divisor += 1

    # Imprimir los factores primos en líneas separadas
    for factor in factores_primos:
        print(factor)

# Solicitar al usuario el número
numero = int(input())

# Obtener la descomposición de factores primos y mostrarlos en líneas separadas
descomposicion_factores_primos(numero)
