def es_primo(numero):
    if (numero == 1):
        return False
    div = range(1, 1000)
    counter = 0
    for x in div:
        value = numero%x
        if (value == 0):
            counter += 1
    if (numero < 1000 and counter <= 2):
        primo = True
    elif (numero > 1000 and counter <= 1):
        primo = True
    else:
        primo = False
    return primo

es_primo(17)