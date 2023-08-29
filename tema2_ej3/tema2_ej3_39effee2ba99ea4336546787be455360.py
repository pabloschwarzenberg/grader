def numero_perfecto(a):
    divisores=[1]
    resultado=0
    for i in range(2,a+1):
        
        if a%i==0:
            divisores.append(i)
            
     
    for i in divisores:
        resultado+=i

    resultado-=a
    
    if resultado==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           