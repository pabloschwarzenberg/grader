def obtener_divisores(numero):
    divisores = [i for i in range(1, numero) if numero % i == 0]
    return divisores

def sumar_divisores(divisores):
    suma = sum(divisores)
    return suma

def son_amigos(a, b):
    divisores_a = obtener_divisores(a)
    divisores_b = obtener_divisores(b)
    
    suma_divisores_a = sumar_divisores(divisores_a)
    suma_divisores_b = sumar_divisores(divisores_b)

    return suma_divisores_a == b and suma_divisores_b == a

# Ejemplo de uso
num1 = 220
num2 = 283

if son_amigos(num1, num2):
    print(f"(num1) y (num2) son números amigos: ")
else:
    print(f"(num1) y (num2) no son números amigos:")
