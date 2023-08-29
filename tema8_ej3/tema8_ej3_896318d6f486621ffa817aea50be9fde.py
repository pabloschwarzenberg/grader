men_imaginary = """

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



def estadisticas_frase(frases_test2):

  frases_test2 = frases_test2.lower()

  puntos_signos = [",",";",".",":","¿","?","!","¡"]

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  #-- Variables test 2 --
  palabras = 0

  caracteres = 0

  test = 0

  etc = 0

  indice = 0

  for x in frases_test2:

    if x in abecedario and frases_test2[indice+1] not in abecedario:

      palabras += 1

    if x in abecedario:

      caracteres += 1

    if x in puntos_signos:

      test += 1

    if x not in abecedario and x not in puntos_signos:

      etc += 1

    indice += 1

  frases2=list(frases_test2)

  new2=len(frases2)

  etc2=0

  for m in frases2:

    if m==" ":

      etc2+=1

  largo_promedio = caracteres/palabras

  return palabras,new2,largo_promedio,etc2,test