def numero_perfecto(numero):
    divide=[1]
    
    for i in range(2,numero):
        if numero%i==0:
            divide.append(i)
    
    suma=sum(divide)    
    if numero==suma:
        return True
    else:
        return False
