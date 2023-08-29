def numeros_amigos(num1, num2):
    def obtener_divisores(n):
        divisores = []
        for i in range(1, n):
            if n % i == 0:
                divisores.append(i)
        return divisores

    suma_divisores_num1 = sum(obtener_divisores(num1))
    suma_divisores_num2 = sum(obtener_divisores(num2))

    if suma_divisores_num1 == num2 and suma_divisores_num2 == num1:
        return True
    else:
        return False


# Ejemplo de uso
r1 = numeros_amigos(1, 2)
print(r1)  # Output: False
