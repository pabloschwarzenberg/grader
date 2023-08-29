def numero_perfecto(a):
    N=0
    for i in range(1,a):
        if a%i==0:
            N=N+i
            
    if N==a:
        return True
    if N!=a:
        return False

           