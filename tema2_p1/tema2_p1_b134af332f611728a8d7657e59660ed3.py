# por favor escribe aquí tu función
def es_primo(n):
    c=2
    if n<2:
      return False
    while c<n:
      if n%c==0:
        return False
      c=c+1
    return True