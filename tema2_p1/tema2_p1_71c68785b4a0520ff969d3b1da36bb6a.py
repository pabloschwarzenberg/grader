def es_primo(numero):
    if numero <= 1:
        es_primo = False
    else:
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break

    return es_primo  

           