# completa el código de la función

def suma_divisores(a):
    lista=[]
    divisor=1
    for i in range(1,a-1):
  
        if a%divisor==0:
           lista.append(divisor)
           divisor=divisor+1
        else:
           divisor=divisor+1
    suma=sum(lista)
    
    
    if suma==1:
        return(suma,True)
    else:
        return(suma,False)
