def es_primo(numero):

    a=0

    for a in range (1, numero+1):
        if numero % a == 0:
            a += 1

    if  a== 2:
        return False

    else:
        return True

print (es_primo(11))

           