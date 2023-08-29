def es_primo(num):
    if num >1:
        div=2
        n=0
        while div<num:
            resto = num%div
            if resto==0:
                n+=1
            div+=1
        if n==0:
            return True
        else:
            return False
    else:
        return False