def son_amigos(a, b):
    def obtener_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores
    
    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))
    if suma_divisores_b == suma_divisores_a:
        return True
    elif suma_divisores_a != suma_divisores_b:
        return False




