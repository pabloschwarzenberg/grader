# completa el código de la función
def son_numeros_amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if son_numeros_amigos(numero1, numero2):
    print("Los números", numero1, "y", numero2, "son números amigos.")
else:
    print("Los números", numero1, "y", numero2, "no son números amigos.")
