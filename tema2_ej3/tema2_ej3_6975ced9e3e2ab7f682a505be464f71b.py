def numero_perfecto(numero):
    divisores = []
    for i in range(1,numero):
        if numero%i == 0:
            divisores.append(i)
    suma = sum(divisores)
    if suma == numero:
        return True
    else:
        return False