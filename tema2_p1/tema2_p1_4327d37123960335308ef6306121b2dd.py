def es_primo(a):
    if a==1:
        return False
    else:
        for n in range(2,a):
            if (a%n)==0:
                return False
        return True