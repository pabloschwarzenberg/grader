def numero_perfecto(numero):
    sumadiv=0
    for i in range(1,numero+1):
        if numero%i==0:
            sumadiv=sumadiv+i
    sumadiv=sumadiv-numero
    if sumadiv==numero:
        a=True
        return a
    else:
        a=False
        return a