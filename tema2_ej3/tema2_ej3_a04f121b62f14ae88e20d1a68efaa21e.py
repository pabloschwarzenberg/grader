def numero_perfecto(a):
    div=1
    suma=0
    if a==1 or a==0:
        return suma,False
    while div<a:
        if a%div==0:
            suma=suma+div
        div+=1
    if suma==a:
        return True
    else:
        return False
   
           