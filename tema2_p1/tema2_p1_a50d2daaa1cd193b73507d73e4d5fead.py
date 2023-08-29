def es_primo(num):
    if(num<=1):
        return False
    B=2
    while(B*B<=num):
        if(num%B==0):
            return False
        B+=1
    return True