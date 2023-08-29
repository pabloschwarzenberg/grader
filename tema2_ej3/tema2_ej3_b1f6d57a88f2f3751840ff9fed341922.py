def numero_perfecto(a):
    a=int(a)
    contador=0
    for i in range(1,a):
        if a%i==0:
            contador+=i
    
        elif a%i!=0:
            contador+=0
                
    if contador==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           