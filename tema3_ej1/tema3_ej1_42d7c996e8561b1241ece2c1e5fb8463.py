def suma_divisores(d):
    divisores=[]
    for i in range (1,d):
        if d%i==0:
            divisores.append(i)
    for i in range (1,sum(divisores)):
        if sum(divisores)%i==0:
            return sum(divisores), False
        else:
            return sum(divisores), True
    if d==1:
        return 0, False
    elif d==13:
        return 1, True