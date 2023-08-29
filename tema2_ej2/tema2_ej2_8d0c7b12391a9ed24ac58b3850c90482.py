# completa el código de la función
def son_amigos(a, b):
    def obtener_divisores(numero):
        divisores = []
        for i in range(1, numero):
            if numero % i == 0:
               divisores+= numero
        return divisores
    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
           