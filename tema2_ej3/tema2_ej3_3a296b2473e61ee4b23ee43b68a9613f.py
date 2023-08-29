def numero_perfecto(numero):
    suma=0
    for r in range(1, numero):
        if numero%r==0:
            suma += r
    return suma == numero