def numero_perfecto(a): 
    suma=0
    for e in range(1,a-1):
         resto=a%e
         if resto==0:
            suma+=e
    if suma==a:
       return True
    else:
       return False