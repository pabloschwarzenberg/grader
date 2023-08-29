
def es_primo(numero):
    flag = 1 
    if numero > 2:
        for W in range(2, numero):
            if (numero % W == 0):
                flag = 0 
                break
    else:
        if numero==2:
            flag = 1
        else:
            flag = 0 
    if flag == 0:
        return False
    else:
        return True