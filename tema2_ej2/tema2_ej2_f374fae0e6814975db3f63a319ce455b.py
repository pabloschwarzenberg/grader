def son_amigos(a, b):
    def suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma

    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    return suma_a == b and suma_b == a


if __name__ == "__main__":
    resultado = son_amigos(1, 2)
    print(resultado)