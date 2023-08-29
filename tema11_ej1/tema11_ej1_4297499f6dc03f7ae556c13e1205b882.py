def palindromo(palabra):
    palabras = []
    def palindromo2(x):
      if len(palabras) < 2:
        palabras.append(x)
        return palindromo2(palabra[::-1])
      else:
        return False
    if not palindromo2(palabra):
        print(palabras)
        if len(set(palabras)) == 1:
          return True
        else:    
          return False
    