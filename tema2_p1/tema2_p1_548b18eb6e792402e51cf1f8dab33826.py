def es_primo(n):

    for i in range (2,n):
        if n%i != 0:
            return True
        else:
            return False
    if n == 1:
        return False