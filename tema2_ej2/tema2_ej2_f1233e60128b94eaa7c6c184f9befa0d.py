def divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    suma_div_a = sum(divisores(a))
    suma_div_b = sum(divisores(b))
    return suma_div_a == b and suma_div_b == a

# Ejemplo de uso
numero1 = 220
numero2 = 284

if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")

           