def numero_perfecto(numero):
    divisor=1
    resto=0
    suma=0
    while divisor<numero:
        resto=numero%divisor
        if resto==0:
            suma+=divisor
        divisor+=1
    if suma==numero:
        return True
    else:
        return False