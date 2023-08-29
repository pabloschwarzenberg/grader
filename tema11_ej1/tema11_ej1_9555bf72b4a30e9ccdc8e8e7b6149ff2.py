def palindromo(palabra):
    if palabra[0]!=palabra[-1]:
        return False
    palabra=palabra[1:-1]
    if len(palabra)<2:
        return True
    return palindromo(palabra)