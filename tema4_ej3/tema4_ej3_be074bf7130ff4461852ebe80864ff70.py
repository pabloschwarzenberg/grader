from cgitb import text


def  jeringonzo(texto):
    n_texto = " " #acumulador 
    for c in texto:
        if c == "a":
            n_texto = n_texto  + c + "p" + c
        elif c == "e":
            n_texto = n_texto  + c + "p" + c
        elif c == "i":
            n_texto = n_texto  + c + "p" + c
        elif c == "o":
            n_texto = n_texto  + c + "p" + c
        elif c == "u":
            n_texto = n_texto  + c + "p" + c
        else: n_texto = n_texto + c
    return n_texto