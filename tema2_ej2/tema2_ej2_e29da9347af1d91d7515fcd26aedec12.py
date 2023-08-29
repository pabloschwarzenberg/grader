def son_numeros_amigos(a, b):
    def calcular_suma_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma
    
    suma_divisores_a = calcular_suma_divisores(a)
    suma_divisores_b = calcular_suma_divisores(b)
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False
