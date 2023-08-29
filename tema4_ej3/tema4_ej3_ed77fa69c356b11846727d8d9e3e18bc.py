def jerigonzo(string):
    pnueva = ""
    for letra in string:
        pnueva = pnueva + letra
        if letra == "a":
            pnueva = pnueva + "pa"
            
        elif letra == "e":
            pnueva = pnueva + "pe"

        elif letra == "i":
            pnueva = pnueva + "pi"

        elif letra == "o":
            pnueva = pnueva + "po"

        elif letra == "u":
            pnueva = pnueva + "pu"

            
    return pnueva


