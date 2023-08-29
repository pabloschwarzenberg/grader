def son_amigos(a, b):
    sum_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    sum_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    
    if sum_divisores_a == b and sum_divisores_b == a:
        return True
    else:
        return False
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if son_amigos(num1, num2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
