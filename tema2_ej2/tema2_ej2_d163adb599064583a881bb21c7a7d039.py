def son_amigos(a, b):
    # Función para obtener la suma de los divisores de un número
    def suma_divisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma

    # Calcular la suma de los divisores de a y b
    suma_div_a = suma_divisores(a)
    suma_div_b = suma_divisores(b)

    # Verificar si son números amigos
    if suma_div_a == b and suma_div_b == a:
        return True
    else:
        return False

# Solicitar al usuario dos números
num_a = int(input("Ingrese el primer número: "))
num_b = int(input("Ingrese el segundo número: "))

# Verificar si los números son amigos
if son_amigos(num_a, num_b):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
