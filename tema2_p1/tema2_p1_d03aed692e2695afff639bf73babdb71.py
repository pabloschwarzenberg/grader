def es_primo(numero):
    if numero == 1:
        Primo = False
    elif numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        if numero == 2 or numero == 3 or numero == 5 or numero == 7:
            Primo = True
        else:
            Primo = False
    else:
        Primo = True
    return(Primo)
