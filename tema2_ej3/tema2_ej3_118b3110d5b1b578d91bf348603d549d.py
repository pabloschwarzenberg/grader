def numero_perfecto(a):
    k=0
    for i in range(1,a):
        if a%i!=0:
            continue
        else:
            k+=i
    if k==a:
        return True
    else:
        return False
           