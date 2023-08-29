def numero_perfecto(a):
    suma=0
    for i in range(1,int(a/2)+1):
        b=a%i
        if b==0:
            suma=suma+i
    if suma==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    b=int(input("suma hasta:"))
    c=0
    for i in range(b):
        numero_perfecto(i)
        if suma==i:
            c=c+i
            
        
    
           