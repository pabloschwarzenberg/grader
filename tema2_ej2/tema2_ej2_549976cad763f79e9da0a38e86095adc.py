def numeros_amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplo de uso
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if numeros_amigos(num1, num2):
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")
