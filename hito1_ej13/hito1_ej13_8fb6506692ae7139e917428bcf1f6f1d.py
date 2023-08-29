#Factores Primos
def factor_primo(num):
    # Inicializamos la lista para almacenar los factores primos
    factores_primos = []

    # Iteramos desde 2 hasta la raíz cuadrada del número
    while num > 1:
        for i in range(2, int(num) + 1):
            if num % i == 0:
                # i es un factor primo, lo añadimos a la lista
                factores_primos.append(i)
                num = num / i
                break

    # Imprimimos los factores primos encontrados
    for factor in factores_primos:
        print(factor)

#Solicitamos al usuario ingresar el número
numero = int(input())

#Descomponemos el número en factores primos
factor_primo(numero)