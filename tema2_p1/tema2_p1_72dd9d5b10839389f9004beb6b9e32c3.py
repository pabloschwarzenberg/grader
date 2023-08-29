def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False
    return True

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print("El número", numero, "es primo.")
    else:
        print("El número", numero, "no es primo.")

           