# por favor escribe aquí tu función
def es_primo(num):

  if num>1:
    a=0
    b=2
    
    while b<num:
      c = num%b
      
      if c==0:
        a+=1
      b+=1

    if a==0:
      return True

    else:
      return False

  else:
    return False          