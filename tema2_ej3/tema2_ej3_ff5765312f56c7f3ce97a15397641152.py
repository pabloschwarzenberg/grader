#NUMERO PERFECTO
def numero_perfecto(a):
    lista=[]
    divisor=1
    for i in range(1,a-1):
  
        if a%divisor==0:
           lista.append(divisor)
           divisor=divisor+1
        else:
           divisor=divisor+1
    suma=sum(lista)
    
    
    if suma==a:
        return(True)
    else:
        return(False)
