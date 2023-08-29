def son_amigos(num1, num2):
    suma_divisores1 = sum(divisor for divisor in range(1, num1) if num1 % divisor == 0)
    suma_divisores2 = sum(divisor for divisor in range(1, num2) if num2 % divisor == 0)
    
    return suma_divisores1 == num2 and suma_divisores2 == num1

# Ejemplo de uso
num1 = 220
num2 = 284
resultado = son_amigos(num1, num2)
print(resultado)  # True
