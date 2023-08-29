def ocultar_letras(palabra,cantidad):
  import random
  from datetime import datetime 
  random.seed(datetime.now())
  #position = random.randint(0,len(lista)-1)
  palabra_secreta = palabra
  cantidad_ocultar = cantidad

  if cantidad_ocultar > len(palabra_secreta):
    cantidad_ocultar = len(palabra_secreta) 
  i = 0
  borrar = []

  while i < cantidad_ocultar:
    aux = random.randint(0,len(palabra_secreta)-1)
    
    while aux in borrar:
      aux = random.randint(0,len(palabra_secreta)-1)
    borrar.append(aux)
    
    i = i + 1
  palabra_final = ""
  for j in range(0,len(palabra_secreta)):
    
    if j in borrar:
      palabra_final = palabra_final + "_"
    else:
      palabra_final = palabra_final + palabra_secreta[j]

  return palabra_final
  
def revisar_letra(palabra_secreta,palabra,letra):
  if len(letra) == 1:
    aux = ""
    pos = 0
    for i in palabra_secreta:
      if letra == palabra_secreta[pos]:
        aux = aux + i
      else:
        aux = aux + palabra[pos]
      pos = pos + 1
    return aux
  else:
    if letra == palabra_secreta: 
      return palabra_secreta
    else:
      return palabra