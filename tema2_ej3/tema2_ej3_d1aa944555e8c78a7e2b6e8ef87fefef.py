def numero_perfecto(a):
    div = 1
    sumadiv=0
    while div < a:
        if int(a)%div==0 and div != 0:
            sumadiv+=div
            div+=1
        else:
            div+=1
    if sumadiv  == a:
        return (True)
    else:
        return(False)
