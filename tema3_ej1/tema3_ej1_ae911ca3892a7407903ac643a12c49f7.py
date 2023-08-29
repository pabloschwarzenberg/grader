# completa el código de la función
def suma_divisores(a):
    suma=0
    for i in range(1,(a-1)):
        c=a%i
        if(c==0):
            suma=suma+i
        elif(c!=0):
            suma=suma
    if(suma==1):
        return(suma,True)
    else:
        return(suma,False)
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(suma_divisores(a))
        