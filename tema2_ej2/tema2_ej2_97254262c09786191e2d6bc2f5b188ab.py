def calcular_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(num1, num2):
    divisores_num1 = calcular_divisores(num1)
    suma_divisores_num1 = sum(divisores_num1)
    
    divisores_num2 = calcular_divisores(num2)
    suma_divisores_num2 = sum(divisores_num2)
    
    if suma_divisores_num1 == num2 and suma_divisores_num2 == num1:
        return True
    else:
        return False

def amigos(num1, num2):
    if son_amigos(num1, num2):
        return True
    else:
        return False

