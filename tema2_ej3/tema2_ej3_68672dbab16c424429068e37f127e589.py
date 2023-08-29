def numero_perfecto(a):
    j=0
    for i in range(1,a):
        if a%i==0:
            j+=i
    if j==a:
        return True
    else:
        return False

