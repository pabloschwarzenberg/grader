def numeros_amigos(a, b):
    suma_divisores_a = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    suma_divisores_b = sum(divisor for divisor in range(1, b) if b % divisor == 0)
    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
numero1 = 220
numero2 = 284

if numeros_amigos(numero1, numero2):
    print(f" { numero1} y {numero2} son numeros amigos.")
else:
    print(f" {numero1} y {numero2} no son numeros amigos.")
