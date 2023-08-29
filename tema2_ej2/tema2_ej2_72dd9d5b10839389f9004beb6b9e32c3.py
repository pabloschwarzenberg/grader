def numeros_amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    return suma_divisores_a == b and suma_divisores_b == a

if __name__ == "__main__":
    numero_a = int(input("Ingrese el primer número: "))
    numero_b = int(input("Ingrese el segundo número: "))

    if numeros_amigos(numero_a, numero_b):
        print("Los números", numero_a, "y", numero_b, "son amigos.")
    else:
        print("Los números", numero_a, "y", numero_b, "no son amigos.")


           