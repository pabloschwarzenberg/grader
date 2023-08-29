def suma_divisores(a):
    j=0
    for i in range(1,a):
        if a%i ==0:
            j=j+i
    if j==1:
        return j,True
    if j != 1:
        return j,False