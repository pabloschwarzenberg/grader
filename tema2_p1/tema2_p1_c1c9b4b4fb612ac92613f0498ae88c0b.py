# por favor escribe aquí tu función
def es_primo(numero):
  i=1
  lista=[]
  while i<=numero:
    if numero%i==0:
      lista.append(i)
    i+=1
  if len(lista)== 2:
    return True
  else:
    return False