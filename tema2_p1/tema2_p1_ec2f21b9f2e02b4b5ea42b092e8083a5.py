# por favor escribe aquí tu función
def es_primo(numero):
  a=1
  lista=[]
  while a<=numero:
    if numero%a==0:
      lista.append(a)
    a+=1
  if len(lista)== 2:
    return True
  else:
    return False