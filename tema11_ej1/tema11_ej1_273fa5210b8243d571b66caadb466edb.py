def palindromo(palabra):
     palabra = list(palabra)
     if palabra == palabra[::-1]:
       return True
     else:
       return False