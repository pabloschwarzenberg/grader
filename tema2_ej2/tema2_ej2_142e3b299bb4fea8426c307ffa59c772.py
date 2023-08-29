# completa el código de la función
def amigos(a,b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)

    return suma_divisores_a == b and suma_divisores_b == a


num1 =1
num2 =2 
if amigos(num1, num2):
    print("Los números", num1, "y", num2, "son amigos.")
else:
    print("Los números", num1, "y", num2, "no son amigos.")
            