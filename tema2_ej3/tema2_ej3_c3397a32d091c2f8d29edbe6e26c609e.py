def numero_perfecto(a):

    def suma_divisores(a):
        suma=0
        sumaDiv=0
        for divisor in range (1,a+1):
            if (a%divisor==0):
                suma+=divisor
                sumaDiv=suma-a
        return sumaDiv
    numerillo=suma_divisores(a)
    if (numerillo==a):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))