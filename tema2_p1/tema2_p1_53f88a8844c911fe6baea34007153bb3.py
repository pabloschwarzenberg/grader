def es_primo(x):
    if x==1:
        return False
    else:
        for i in range(2,x):
            if x%i==0:
                return False
            elif x%i!=0:
                return True
