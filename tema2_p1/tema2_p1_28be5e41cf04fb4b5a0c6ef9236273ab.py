def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar si el número es primo
es_primo_resultado = es_primo(numero)

# Imprimir el resultado
if es_primo_resultado:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
