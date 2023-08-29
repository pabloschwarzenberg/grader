def palindromo(palabra):
    l = len(palabra)
    if l==1 or l==0:
        return True
    elif palabra[0] != palabra[1:(l-1)]:
        return False
    else:
        nueva_palabra = palabra[1:(l-1)]
        palindromo(nueva_palabra)
