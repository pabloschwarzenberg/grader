def es_primo(numero):
    if numero < 2:  # Los números menores que 2 no son primos
        return False

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False

    return True

numero = int(input("Ingresa un número: "))

if es_primo(numero):
    print("True")
else:
    print("False")
      