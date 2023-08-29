def es_primo(numero):
    for n in range(2, numero):
       if numero % n == 0:
           return False
    if numero==1:
      return False
    else:
      return True