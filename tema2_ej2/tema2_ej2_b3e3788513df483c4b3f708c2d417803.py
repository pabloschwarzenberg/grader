def son_amigos(a, b):
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)

    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
resultado = son_amigos(num1, num2)
print(resultado)