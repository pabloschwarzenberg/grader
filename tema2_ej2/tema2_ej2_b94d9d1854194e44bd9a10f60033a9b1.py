def son_amigos(a, b):
    def obtener_divisores(num):
        divisores = []
        for i in range(1, num):
            if num % i == 0:
                divisores.append(i)
        return divisores

    suma_a = sum(obtener_divisores(a))
    suma_b = sum(obtener_divisores(b))

    return suma_a == b and suma_b == a

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if son_amigos(num1, num2):
    print("Son números amigos")
else:
    print("No son números amigos")
