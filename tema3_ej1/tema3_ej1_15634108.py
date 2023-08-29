def suma_divisores(a):
    if a==1:
        return 0,False
    else:
        sumadiv=1
        for i in range(2,a):
            if a%i==0:
                sumadiv=sumadiv+i
            else:
                pass
        if sumadiv==1:
            return sumadiv,True
        else:
            return sumadiv,False
