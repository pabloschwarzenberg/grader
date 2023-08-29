# por favor escribe aquí tu función
def es_primo(numero):
  
  a=1

  while a<=numero:
    if numero==1:
        return True
    elif a==numero:
        return True
    elif numero%a==0 and numero!=a and a!=1:
        return False
        break
    a=a+1
           