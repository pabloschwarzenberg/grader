def suma_divisores(numero):
    sumaDivisores=0 
    for i in range(1,numero-1,1): 
        if numero%i==0:
            sumaDivisores=sumaDivisores+i 
    if sumaDivisores==1:
        return sumaDivisores,True
    
    return sumaDivisores,False
if "_name_"=="_main_":
    numero=int(input("ingrese numero: "))
    print(suma_divisores(numero))