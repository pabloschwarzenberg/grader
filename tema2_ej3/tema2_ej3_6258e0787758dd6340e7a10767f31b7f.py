def numero_perfecto(num):
    cont=1
    suma=0
    while cont!=num:
        if num%cont==0:
            suma=suma+cont
        cont=cont+1
    if suma==num:
        return True
    else:
        return False
           