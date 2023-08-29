# completa el código de la función
def suma_divisores(a):
    
    suma=0
    for i in range(1,a):
        if a%i==0:
            print(i)
            suma=suma+i  
    if 1==suma:
        return suma,True 
    else:
        return suma,False
           