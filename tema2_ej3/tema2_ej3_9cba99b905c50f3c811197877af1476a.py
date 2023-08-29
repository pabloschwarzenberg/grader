def numero_perfecto(numero):
    contador=1
    suma=0
    while contador!=numero:
        if numero%contador==0:
            suma=suma+contador
        contador=contador+1
    if suma==numero:
        return True
    else:
        return False

           