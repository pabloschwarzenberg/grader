def numero_perfecto(numero):
    divisores=[1]
    for n in range(2,numero):
        if numero%n==0:
            divisores.append(n)
    suma=sum(divisores)    
    if numero==suma:
        return True
    else:
        return False
