def numero_perfecto(a):
    contador = a
    suma = 0
    while(contador != 1):
        divisor = a/contador
        if(int(divisor) == divisor):
            suma = suma + divisor
            contador = contador - 1
        else:
            contador = contador - 1
    if(a == suma ):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           