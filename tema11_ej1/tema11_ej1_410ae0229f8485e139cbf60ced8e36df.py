def palindromo(palabra):
    palabra=list(palabra)
    if len(palabra)==0 or len(palabra)==1:
      return True
    else:
      x=palabra.pop(0)
      y=palabra.pop()
      if x==y:
        return palindromo(palabra)
      else:
        return False

           