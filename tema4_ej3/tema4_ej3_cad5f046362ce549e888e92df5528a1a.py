def jerigonzo(texto):
    n_texto = ""
    for c in texto:
        if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
            n_texto = n_texto + c + "p" + c
        else:
            n_texto = n_texto + c
    return n_texto