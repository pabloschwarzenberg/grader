def numero_perfecto(numero):
    divisor=1
    suma=0
    while divisor<numero:
        if numero%divisor==0:
            suma+=divisor
            divisor+=1
        else:
            divisor+=1
    if suma==numero:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))