def numero_perfecto(numero):
    token=1
    suma=0
    while token!=numero:
        if numero%token==0:
            suma=suma+token
        token=token+1
    if suma==numero:
        return True
    else:
        return False