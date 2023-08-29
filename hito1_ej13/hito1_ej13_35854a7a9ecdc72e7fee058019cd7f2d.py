#Factores Primos
def factorizar(numero):
    # Iteramos desde 2 hasta la mitad del número, ya que ningún factor primo puede ser mayor que su mitad
    for i in range(2, numero // 2 + 1):
        while numero % i == 0:
            # Imprimimos el factor primo
            print(i)
            numero = numero // i

    # Si después del ciclo aún nos queda un número mayor que 1, significa que ese número también es primo
    if numero > 1:
        print(numero)

# Solicitamos al usuario que ingrese un número
numero = int(input())

# Llamamos a la función para realizar la factorización
factorizar(numero)      