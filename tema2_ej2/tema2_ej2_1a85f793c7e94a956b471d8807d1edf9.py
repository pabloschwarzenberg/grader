def amigos(num1, num2):
    def obtener_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_num1 = sum(obtener_divisores(num1))
    suma_divisores_num2 = sum(obtener_divisores(num2))

    if suma_divisores_num1 == num2 and suma_divisores_num2 == num1:
        return True
    else:
        return False

resultado = amigos(220, 284)
print(resultado)
