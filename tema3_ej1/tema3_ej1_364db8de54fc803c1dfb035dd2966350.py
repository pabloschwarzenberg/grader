# completa el código de la función
#suma de divisores
def suma_divisores(a):
    divisor=[1]
    for i in range(2,a): 
        if a%i==0:
            divisor.append(i)
    suma=sum(divisor) 
    if suma==1:
        if a ==1:
            return(0,False)
        else:
            return(suma,True)
    else:  
        return(suma,False)
print("Fin")
