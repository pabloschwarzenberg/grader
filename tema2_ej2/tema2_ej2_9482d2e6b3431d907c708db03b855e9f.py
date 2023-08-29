# completa el código de la función
def son_amigos(a, b):
    # Función para calcular la suma de los divisores de un número
    def suma_divisores(numero):
        suma = 0
        for i in range(1, numero):
            if numero % i == 0:
                suma += i
        return suma

    # Calculamos la suma de los divisores de 'a' y 'b'
    suma_a = suma_divisores(a)
    suma_b = suma_divisores(b)

    # Verificamos si son números amigos
    if suma_a == b and suma_b == a:
        return True
    else:
        return False

# Pedimos al usuario que ingrese dos números
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Llamamos a la función para verificar si los números son amigos
if son_amigos(numero1, numero2):
    print("Los números", numero1, "y", numero2, "son amigos.")
else:
    print("Los números", numero1, "y", numero2, "no son amigos.")
