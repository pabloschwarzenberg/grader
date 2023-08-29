def palindromo(palabra):
    if len(palabra) == 1:
        return True
    elif len(palabra) == 0:
        return True

    else:
        if palabra[0] != palabra[-1]:
            return False
        else:
            return palindromo(palabra[1:-1])




