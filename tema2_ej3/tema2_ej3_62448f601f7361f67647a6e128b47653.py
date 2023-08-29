#número perfecto

def numero_perfecto(a):
    suma_divisores = 0
    if a == 0 or a == 1:
        return False
    for divisores in range(1, a):
        if a%divisores == 0:
            suma_divisores += divisores
    if suma_divisores == a:
        return True
    else:
        return False

if __name__=="__main__":

    x = int(input("Ingrese x: "))
    print(numero_perfecto(x))
           