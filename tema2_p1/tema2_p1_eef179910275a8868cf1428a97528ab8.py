# por favor escribe aquí tu función
def es_primo(numero):
    div=0
    for i in range(2,numero):
      if numero%i==0:
        div+=1
        break
    if numero==1:
        return False
    elif div==0:
        return True
    else:
        return False