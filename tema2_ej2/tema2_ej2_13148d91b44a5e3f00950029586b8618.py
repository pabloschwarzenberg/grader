def son_amigos(a, b):
    def calcular_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores.append(i)
        return divisores

    r1=self.modulo.amigos(1,2) -> 'module' object has no attribute 'amigos'
SubmitSome problems have options such as save, reset, hints, or show answer. These options follow the Submit button.
    suma_divisores_b = sum(calcular_divisores(b))

    return suma_divisores_a == b and suma_divisores_b == a


           