def amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    if suma_divisores(a) == b and suma_divisores(b) == a:
        return True
    else:
        return False

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

print('\n¿Los números son amigos?')

if amigos(numero1, numero2):
    print("True")
else:
    print("False")