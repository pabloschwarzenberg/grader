from random import randint, uniform,random

def ocultar_letras(palabra,cantidad):

  indices=[]

  for i in range(cantidad):

    indice = randint(0,len(palabra)-1)

    if len(indices)==0:
      indices.append(indice)
    else:
      encontro = 0
      for x in indices:
        if indice == x:
          encontro=1
          break
      
      if encontro==1:
        i=i-1
      else:
        indices.append(indice)

  i=0

  palabraocultada=""
  for i in range(len(palabra)):
   
    #ocultar?
    ocultar = 0
    for x in indices:
      if i == x:
        ocultar=1
        break
      else:
        ocultar=0
    
    if ocultar ==1:
      palabraocultada = palabraocultada + "_"
    else:
      palabraocultada = palabraocultada + palabra[i]
      
  #print(palabraocultada)      

  return palabraocultada 

def revisar_letra(palabra_secreta,palabra,letra):
  mostrar = ""
  x=0
  for i in palabra_secreta:
    if i == letra:
      mostrar = mostrar + letra
    else:
      mostrar = mostrar + palabra[x]
    x=x+1
  #print(mostrar)   
  return mostrar




palabras =["JUEGOS","PALABRAS","FOME","QUIERO","UN","SIETE"]

palabrajugar = palabras[randint(0,len(palabras)-1)]
palabrajugar = palabras[0]

letrasocultar = randint(1,len(palabrajugar)-1)

palabra_oculta=(ocultar_letras(palabrajugar,letrasocultar))

palabra_revisada=revisar_letra(palabrajugar,palabra_oculta,"J")
         