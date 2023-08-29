# completa el código de la función
def suma_divisores(a):
    suma = 0
    res = False
    for i in range(1,a):
        if a%i == 0:
            suma += i
    for j in range(2,suma):
        if (suma%j)==0:
            return (suma,False)       
    return (suma,True)



            
           