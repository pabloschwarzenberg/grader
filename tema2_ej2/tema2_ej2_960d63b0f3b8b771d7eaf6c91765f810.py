def son_amigos(a, b):
    sum_div_a = sum([i for i in range(1, a) if a % i == 0])
    sum_div_b = sum([i for i in range(1, b) if b % i == 0])
    
    return sum_div_a == b and sum_div_b == a

# Ejemplo de uso
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if son_amigos(numero_1, numero_2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
