def suma_divisores(a):
    i=1
    resultado=0
    for x in list(range(1,a)):
        if a%i==0:
            resultado=resultado+i
        i=i+1
    if resultado==1:
        return (resultado,True)
    else:
        return (resultado,False)
