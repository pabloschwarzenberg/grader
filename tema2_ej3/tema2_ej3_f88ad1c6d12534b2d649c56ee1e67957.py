## ENTRADA DE DATOS - PROCESO - SALIDA

def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


if __name__ == "__main__":
    numero = int(input("Ingrese un numero: "))
    if numero_perfecto(numero):
        print(numero, "es numero perfecto")
    else:
        print(numero, "No es numero perfecto")
           