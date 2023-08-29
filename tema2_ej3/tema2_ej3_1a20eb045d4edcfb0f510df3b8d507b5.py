def numero_perfecto(a):
    divisores=[]

    for i in range(1,a+1):
        if a%i==0:
            if i!=a:
                 divisores.append(i)
    if sum(divisores)==a:
        return True
    else:
        return False 
