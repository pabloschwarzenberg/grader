def numero_perfecto(a):
    x=a
    divisores_suma=0
    for i in range(x):
        resto=a%x        
        if resto==0:
            divisores_suma+=x
        x-=1
    if (divisores_suma-a)==a:
        return True
    elif (divisores_suma-a)!=a:
        return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           