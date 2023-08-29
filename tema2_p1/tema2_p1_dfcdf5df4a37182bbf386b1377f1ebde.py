def es_primo(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            elif (i==n-1):
                return True


           