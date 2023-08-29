def numero_perfecto(a):
    divisores=0
    if a==1:
        return(False)
    for i in range (1 , a+1):
        if a%i==0 and i!=a:
            divisores=divisores+(i)
    if divisores==a:
        return (True) 
    elif divisores!=a:
        return(False)