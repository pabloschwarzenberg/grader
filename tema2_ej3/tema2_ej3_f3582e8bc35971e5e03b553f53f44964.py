def numero_perfecto(a):
    suma=0
    i=1
    if a==1:
        return True
    if a==0:
        return False
    while i<a:
        if a%i==0:
            suma+=i
        i+=1
        
    if suma==a:
        return True
    else:    
        return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           