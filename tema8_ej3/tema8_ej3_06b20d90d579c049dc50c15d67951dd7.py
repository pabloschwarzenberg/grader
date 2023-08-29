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

  puntuacion = [":",";",".",",","¡","!","¿","?"]

  letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","í","é","ó","ú"]

  palabras = 0

  caracteres = 0

  puntuacion_2 = 0

  espacios = 0

  individuales = 0

  for i in frase:

    if i in letras and frase[individuales+1] not in letras:

      palabras += 1

    if i in letras:

      caracteres += 1

    if i in puntuacion:

      puntuacion_2 += 1

    if i not in letras and i not in puntuacion:

      espacios += 1

    individuales += 1

  frase_2 =list(frase)

  nuevo =len(frase_2)

  espacios_2= 0

  for j in frase_2:

    if j==" ":

      espacios_2 += 1

  largo = caracteres/palabras

  return palabras,nuevo,largo,espacios_2,puntuacion_2