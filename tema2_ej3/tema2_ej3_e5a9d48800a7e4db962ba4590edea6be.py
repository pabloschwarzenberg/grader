def numero_perfecto(a):
    cont=1
    suma=0
    while cont<a-1:
        if a%cont==0:
            suma+=cont
        cont+=1
    if suma==a:
        return True
    else:
        return False
            
            
