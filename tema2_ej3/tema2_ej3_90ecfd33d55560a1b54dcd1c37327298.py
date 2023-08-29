def numero_perfecto(a):
    count = 1
    suma1 = 0
    while count != a:
        if a % count == 0:
            suma1 = suma1 + count
        count = count + 1
    if suma1 == a:
        return True
    else:
        return False


if __name__ == "__main__":
    a = eval(input("Ingrese un número: "))
    if numero_perfecto(a):
        print("{0} es un número perfecto".format(a))
    else:
        print("{0} no es un número perfecto".format(a))
