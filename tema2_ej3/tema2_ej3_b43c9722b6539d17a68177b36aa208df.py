def numero_perfecto(numero):
    divisor=[1]
    
    for i in range(2,numero):
        if numero%i==0:
            divisor.append(i)
    
    suma=sum(divisor)    
    if numero==suma:
        return True
    else:
        return False           