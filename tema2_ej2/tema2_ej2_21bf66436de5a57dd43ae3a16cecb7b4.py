def divisores(numero):
    lista_divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def son_amigos(a, b):
    suma_divisores_a = sum(divisores(a))
    suma_divisores_b = sum(divisores(b))
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False