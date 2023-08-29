def suma_divisores(a):
    S=0
    for i in range(1,a):
        if a%i==0:
            S=S+i
    if S==1:
        return (S,True)
    else:
        return (S,False)
    
           