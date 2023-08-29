def numero_perfecto(d):
    divisores=[]
    for i in range (1,d):
        if d%i==0:
            divisores.append(i)
    if sum(divisores)==d:
        numero_perfecto=True
        return True
    else:
        numero_perfecto=False
        return False