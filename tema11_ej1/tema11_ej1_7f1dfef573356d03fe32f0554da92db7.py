def palindromo(palabra):
    palabra = list(palabra)
    pa = list(palabra)
    palabra.reverse()
    return pa == palabra