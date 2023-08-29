def numero_perfecto(l):
    divisor=1
    suma=0
    for i in range(1,l):
        if l%divisor==0:
            suma+=divisor
        divisor+=1
    if suma==l:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           