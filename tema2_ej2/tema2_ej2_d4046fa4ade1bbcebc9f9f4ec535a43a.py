def obtener_divisores(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

def son_amigos(num1, num2):
    suma_divisores_num1 = sum(obtener_divisores(num1))
    suma_divisores_num2 = sum(obtener_divisores(num2))

    return suma_divisores_num1 == num2 and suma_divisores_num2 == num1

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
