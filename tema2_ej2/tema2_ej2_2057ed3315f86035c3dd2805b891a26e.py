
def son_numeros_amigos(a, b):
    # Calcula la suma de los divisores de 'a'
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)

    # Calcula la suma de los divisores de 'b'
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)

    # Verifica si las sumas de los divisores son iguales y diferentes de los números originales
    if suma_divisores_a == b and suma_divisores_b == a and a != b:
        return True
    else:
        return False