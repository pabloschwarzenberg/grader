def numero_perfecto(a):
    suma_divisores = 0
    for divisor in range(1,a):
        if a/divisor == int(a/divisor):
            suma_divisores += divisor
    if suma_divisores == a:
        return True
    return False
if __name__ == '__main__':
    a=int(input("Ingrese un número: "))
    print(numero_perfecto(a))
           