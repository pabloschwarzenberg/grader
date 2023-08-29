def numero_perfecto(a):
    B=0
    for i in range(1,a):
        if a%i==0:
            B+=i
    if B==a:
        return True
    if B!=a:
        return False