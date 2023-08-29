# completa el código de la función
def numeros_amigos(a, b):
    def obtener_divisores(n):
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return False
    else:
        return True