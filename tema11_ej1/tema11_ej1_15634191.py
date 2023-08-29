def palindromo(palabra):
    if len(palabra)<2:
        return True
    elif palabra[0]==palabra[-1]:
        palabra=palabra.rstrip(palabra[-1])
        palabra=palabra.lstrip(palabra[0])
        return palindromo(palabra)
    else:
        return False
