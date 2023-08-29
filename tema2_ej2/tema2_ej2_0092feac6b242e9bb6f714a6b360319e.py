def obtener_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def amigos(a, b):
    suma_divisores_a = sum(obtener_divisores(a))
    suma_divisores_b = sum(obtener_divisores(b))
    
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

# Ejemplo de uso
numero1 = 220
numero2 = 284

if amigos(numero1, numero2):
    print(numero1, "y", numero2, "son números amigos")
else:
    print(numero1, "y", numero2, "no son números amigos")   