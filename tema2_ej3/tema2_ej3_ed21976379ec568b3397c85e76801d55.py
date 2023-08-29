def numero_perfecto(a):
    
    divisores=[]
    for i in range(1,a):
        divide=a%i
        if(divide==0):
            divisores.append(i)
            
    suma=sum(divisores)
    if (suma==a):
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

           