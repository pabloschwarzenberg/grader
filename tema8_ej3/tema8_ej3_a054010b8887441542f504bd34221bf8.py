hombre_imaginario = """

El hombre imaginario

vive en una mansión imaginaria

rodeada de árboles imaginarios

a la orilla de un río imaginario



De los muros que son imaginarios

penden antiguos cuadros imaginarios

irreparables grietas imaginarias

que representan hechos imaginarios

ocurridos en mundos imaginarios

en lugares y tiempos imaginarios



Todas las tardes tardes imaginarias

sube las escaleras imaginarias

y se asoma al balcón imaginario

a mirar el paisaje imaginario

que consiste en un valle imaginario

circundado de cerros imaginarios..."""



def estadisticas_frase(frase):

  frase = frase.lower()
  
#sombolos de palabras
  acen = [",",";",".",":","¿","?","!","¡"]
#abecedario
  let = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  tra = 0

  txt = 0
  

  tup = 0
  

  sub = 0
  

  pro = 0
  

  for i in frase:

    if i in let and frase[pro+1] not in let:

      tra += 1

    if i in let:

      txt += 1

    if i in acen:

      tup += 1

    if i not in let and i not in acen:

      sub += 1

    pro += 1

  frase2=list(frase)

  new2=len(frase2)

  esp2=0

  for a in frase2:

    if a==" ":

      esp2+=1

  corto = txt/tra

  return tra,new2,corto,esp2,tup



#if _name_ == "_main_":

#print(estadisticas_frase(hombre_imaginario))



from string import ascii_letters