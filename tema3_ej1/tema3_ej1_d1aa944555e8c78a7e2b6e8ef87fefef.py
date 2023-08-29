def suma_divisores(a):
    div = 1
    sumadiv=0
    while div < a:
        if int(a)%div==0 and div != 0:
            sumadiv+=div
            div+=1
        else:
            div+=1
    if sumadiv  == 1:
        return (sumadiv,True)
    else:
        return(sumadiv,False)
