def obtener_divisores(n):
    divisores = []
    for i in range(1, n):
        if n % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(a, b):
    suma_a = sum(obtener_divisores(a))
    suma_b = sum(obtener_divisores(b))
    return suma_a == b and suma_b == a

numero1 = 258
numero2 = 258

if son_amigos(numero1, numero2):
    print(f"Los números {numero1} y {numero2} son números amigos.")
else:
    print(f"Los números {numero1} y {numero2} no son números amigos.")