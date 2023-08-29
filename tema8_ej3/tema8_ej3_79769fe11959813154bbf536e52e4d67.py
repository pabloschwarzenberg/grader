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

  frase_one = frase.lower()

  teclas_especiales = [",",";",".",":","¿","?","!","¡"]

  Diccionary = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

                "n","o","p","q","r","s","t","u","v","w","x","y","z",

                "á","í","é","ó","ú"]

  words = 0

  charact = 0

  puntos = 0

  spa = 0

  verif = 0

  for i in frase_one:

    if i in Diccionary and frase[verif+1] not in Diccionary:

      words += 1

    if i in Diccionary:

      charact += 1

    if i in teclas_especiales:

      puntos += 1

    if i not in Diccionary and i not in teclas_especiales:

      spa += 1

    verif += 1

  fras_two=list(frase_one)

  nuevo =len(fras_two)

  spatwo=0

  for e in fras_two:

    if e ==" ":

      spatwo+=1

  aver_largo = charact/words

  return words,nuevo,aver_largo,spatwo,puntos



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))

         