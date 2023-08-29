def es_primo(numero):
  if numero >1:
    f=0
    divi_sor=2
    while divi_sor<numero:
      resto = numero%divi_sor
      if resto==0:
        f+=1
      divi_sor+=1
    if f==0:
      return True
    else:
      return False
  else:
    return False        