def numero_perfecto(a):
    divisores=[]
    for i in range (1,a):
        if a%i==0:
            divisores.append(i)
    if sum(divisores)==a:
        numero_perfecto=True
        return True
    else:
        numero_perfecto=False
        return False
