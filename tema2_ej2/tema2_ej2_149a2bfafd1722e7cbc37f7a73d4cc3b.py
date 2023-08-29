def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero//2 + 1):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a
        return True
    else:
        return False
  