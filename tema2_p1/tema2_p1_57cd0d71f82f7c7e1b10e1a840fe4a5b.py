def es_primo(x):
    divisores=0
    if x==1 or x==0:
        return False
    elif x>1:
        for i in range(2,x-1):
            if x%i==0:
                divisores=divisores+1
    if divisores==0:
        return True
    else:
        return False

        