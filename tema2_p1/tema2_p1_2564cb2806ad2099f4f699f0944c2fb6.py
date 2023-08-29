# por favor escribe aquí tu función
def es_primo(a):
    if(2<a):
      for p in range(2,a):
        if(a%p!=0):
         return True
        else:
             return False
    else:
      return False
           