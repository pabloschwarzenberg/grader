def suma_divisores(numero):
    sumadiv=0
    for i in range(1,numero+1):
        if numero%i==0:
            sumadiv=sumadiv+i
    sumadiv=sumadiv-numero
    if sumadiv==1:
        A=True
        return (sumadiv,A)
    else:
        A=False
        return (sumadiv,A)
           