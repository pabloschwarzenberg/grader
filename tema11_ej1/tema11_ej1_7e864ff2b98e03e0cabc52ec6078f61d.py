def palindromo (palabraa):
    if len(palabraa) == 1 or len(palabraa) == 0:
        return True
    elif palabraa[0] == palabraa[-1]:
        return palindromo(palabraa[1:-1])
    else:
        return False