def numero_perfecto(f):
    p=1
    suma=0
    while p<f:

        if f%p==0:
            suma=suma+p
            p=p+1
        else:
            p=p+1
    if suma==f:
        return True
    if suma!=f:
        return False



           