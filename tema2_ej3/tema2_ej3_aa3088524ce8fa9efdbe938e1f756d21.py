def numero_perfecto(a):
    suma_divisores= 0
    for i in range(1, a):
        if a % i == 0:
            suma_divisores += i
    if suma_divisores == a:
        return True
    else:
        return False
#principal
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    if numero_perfecto(a):
        print(a, "es un número perfecto.")
    else:
        print(a, "no es un número perfecto.")
           