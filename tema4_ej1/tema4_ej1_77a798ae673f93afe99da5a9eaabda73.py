import random
def ocultar_letras(palabra,cantidad):
  ocultar=0
  lista=[]
  while ocultar<cantidad:
    lugar=random.randint(0,cantidad-1)
    if lista.count(lugar)== 0:
      lista.append(lugar)
      palabra_1=list(palabra)
      palabra_1[lugar]="_"
      palabra="".join(palabra_1)
      ocultar=ocultar+1
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  if (letra in palabra_secreta)==1:
    n=0
    lugar=[]
    while n <len(palabra):
      if palabra_secreta[n]==letra:
        lugar.append(n)
      n=n+1
    palabracompleta=list(palabra)
    for luga in lugar:
      palabracompleta[luga]=letra
    palabrajunta="".join(palabracompleta)
    return (palabrajunta)


         