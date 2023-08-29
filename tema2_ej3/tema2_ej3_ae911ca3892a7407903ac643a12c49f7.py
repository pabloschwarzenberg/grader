def numero_perfecto(a):
    suma=0
    for i in range(1,(a-1)):
        c=a%i
        if(c==0):
            suma=suma+i
        elif(c!=0):
            suma=suma
    if(suma==a):
        return True
    elif(suma!=0):
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))       