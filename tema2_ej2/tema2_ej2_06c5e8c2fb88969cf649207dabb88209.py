import modulo

r1 = modulo.amigos(1, 2)
print(r1)
def numeros_amigos(a, b):
    def sum_divisores(num):
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        return suma
    
    suma_a = sum_divisores(a)
    suma_b = sum_divisores(b)
    
    return suma_a == b and suma_b == a

# Ejemplo de uso
print(numeros_amigos(220, 284))  # Devuelve True
print(numeros_amigos(1184, 1210))  # Devuelve True
print(numeros_amigos(6, 28))  # Devuelve False

print(numeros_amigos(1184, 1210))  # Devuelve True
print(numeros_amigos(6, 28))  # Devuelve False
print(numeros_amigos(1184, 1210))  # Devuelve True
print(numeros_amigos(6, 28))  # Devuelve False