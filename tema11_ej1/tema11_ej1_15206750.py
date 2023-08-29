def palindromo(palabra):
    palabra_l = list(palabra)
    if len(palabra_l) == 1 or len(palabra_l) == 0:
        return True
    else:
        if palabra_l[0] == palabra_l[len(palabra_l)-1]:
            palabra_l = palabra_l[1:]
            palabra_l = palabra_l[:len(palabra_l)-1]
            palabra = palabra_l
            return palindromo(palabra)
        else :
            return False