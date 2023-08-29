# completa el código de la función
def suma_divisores(a):
    
    divisores=[1-a]
    for i in range(2,a+1):
        if a%i==0:
            divisores.append(i)
            
    divi=sum(divisores)
    if divi==1:
        return divi,True
    else:
        return divi,False
    pass


if __name__ == "__main__":
    b=int(input("Seleccion su divisor -> "))
    c=suma_divisores(b)
    print(c)
    
    pass