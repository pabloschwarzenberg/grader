# completa el código de la función
def amigos(a, b):
    def divisores(numero):
        divisores_lista = []
        for i in range(1, numero):
            if numero % i == 0:
                divisores_lista.append(i)
        return divisores_lista

    suma_divisores_a = sum(divisores(a))
    suma_divisores_b = sum(divisores(b))

    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    
    return False