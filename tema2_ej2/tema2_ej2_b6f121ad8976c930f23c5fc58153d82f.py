# completa el código de la función
def amigos(a,b):
    if a == b:
        return False

    suma_divisores_a = sum([divisor for divisor in range(1, a) if a % divisor == 0])
    suma_divisores_b = sum([divisor for divisor in range(1, b) if b % divisor == 0])

    return suma_divisores_a == b and suma_divisores_b == a

if __name__ == "__main__":
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    if amigos(numero1, numero2):
        print("Son números amigos")
    else:
        print("No son números amigos")

           