def suma_divisores(x):
    i=0
    A=0
    while i<x-1:
        j=0
        i=i+1
        if x%i==0:
            j=i+j
        else:
            j=0
        A=j+A
    M=True
    if A!=1:
        M=False
    return A,M