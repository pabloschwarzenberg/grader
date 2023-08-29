def divisores(num):
    """Función auxiliar para obtener la lista de divisores de un número."""
    lista_divisores = []
    for i in range(1, num):
        if num % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def son_amigos(a, b):
    """Verifica si dos números son amigos."""
    suma_divisores_a = sum(divisores(a))
    suma_divisores_b = sum(divisores(b))
    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if son_amigos(num1, num2):
    print("{} y {} son números amigos.".format(num1, num2))
else:
    print("{} y {} no son números amigos.".format(num1, num2))

