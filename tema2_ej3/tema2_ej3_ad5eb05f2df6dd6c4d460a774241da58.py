def numero_perfecto(a):
    divisor=1
    sumaDivisor=0
    while divisor<a:
        if a%divisor==0:
            sumaDivisor+=divisor
        divisor+=1
    if sumaDivisor==a:
        return True
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))