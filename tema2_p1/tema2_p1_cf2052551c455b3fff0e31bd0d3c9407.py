def es_primo(numero):
    primo = False
    if numero > 1:

        for i in range(2, int(numero/2)+1):


            if (numero % i) == 0:
                primo = False
                break
        else:
            primo = True

    else:
        primo = False

        

    return primo
