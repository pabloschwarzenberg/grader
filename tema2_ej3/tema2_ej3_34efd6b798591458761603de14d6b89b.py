def numero_perfecto(a):
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    if numero_perfecto(num):
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto.")
          