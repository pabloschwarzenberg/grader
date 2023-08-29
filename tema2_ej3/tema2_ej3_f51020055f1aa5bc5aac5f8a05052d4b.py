def numero_perfecto(a):
    numero = a
    suma_divisores = 0
    
    for divisor in range(1,numero+1):
        if (numero % divisor) == 0 and divisor!=numero:
            suma_divisores += divisor

    if suma_divisores==numero:
        return True
    else:
        return False
        
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           