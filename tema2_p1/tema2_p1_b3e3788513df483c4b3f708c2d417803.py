def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejemplo de uso
numero = int(input("Ingrese un número: "))
resultado = es_primo(numero)
print(resultado)
else:
    print(numero, "no es primo")