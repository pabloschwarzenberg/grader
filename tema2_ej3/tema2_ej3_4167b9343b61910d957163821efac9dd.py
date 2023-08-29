def numero_perfecto(num):
    suma_divisores = sum(divisores(num))
    return suma_divisores == num

def divisores(num):
    divisores = []
    for i in range(1, num):
        if num % i == 0:
            divisores.append(i)
    return divisores

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print("El número", numero, "es un número perfecto.")
    else:
        print("El número", numero, "no es un número perfecto.")
