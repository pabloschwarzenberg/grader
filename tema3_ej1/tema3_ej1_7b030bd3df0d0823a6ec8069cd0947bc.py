# completa el código de la función
def suma_divisores(a):
    contador = a
    suma = 0
    while contador != 1:
        divisor = a/contador 
        if(int(divisor) == divisor):
            suma = suma + divisor
            contador = contador - 1
        else:
            contador = contador - 1
    a = int(suma)
    global b
    b = a
    if a == 1:
        print("a=1",a)
        return a,True
    else:
        print("a=0",a)
        return a,False

      
if __name__ == "__main__":
    a = int(input("Ingrese un numero: "))
    suma_divisores(a)
    if(b == 1):
        print("ES NUMERO PRIMO")
    else:
        print("NO ES NUMERO PRIMO")