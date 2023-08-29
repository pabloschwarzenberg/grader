def amigos(a, b):
    def calcular_suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    suma_div_a = calcular_suma_divisores(a)
    suma_div_b = calcular_suma_divisores(b)

    return suma_div_a == b and suma_div_b == a
    
numero1 = 220
numero2 = 284

if amigos(numero1, numero2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")