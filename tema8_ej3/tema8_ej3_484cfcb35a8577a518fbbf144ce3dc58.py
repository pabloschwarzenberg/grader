hombre_imaginario = """

El hombreimaginario

vive en una mansión imaginaria

rodeada de árboles imaginarios

a la orilla de un río imaginario



De los muros que son imaginarios

penden antiguos cuadrosimaginarios

irreparables grietas imaginarias

que representan hechos imaginarios

ocurridos en mundos imaginarios

en lugares y tiempos imaginarios



Todas las tardes tardes imaginarias

sube las escaleras imaginarias

y se asoma albalcón imaginario

a mirar el paisaje imaginario

que consiste en un valle imaginario

circundado de cerros imaginarios..."""



def estadisticas_frase(palabra):

  palabra = palabra.lower()

  signos = [",",";",".",":","¿","?","!","¡"]

  abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m",

      "n","o","p","q","r","s","t","u","v","w","x","y","z",

      "á","í","é","ó","ú"]

  one = 0

  two = 0

  three = 0

  four = 0

  five = 0

  for i in palabra:

    if i in abecedario and palabra[five+1] not in abecedario:

      one += 1

    if i in abecedario:

      two += 1

    if i in signos:

      three += 1

    if i not in abecedario and i not in signos:

      four += 1

    five += 1

  frase2=list(palabra)

  new2=len(frase2)

  esp2=0

  for e in frase2:

    if e==" ":

      esp2+=1

  prom_largo = two/one

  return one,new2,prom_largo,esp2,three



if __name__ == "__main__":

  print(estadisticas_frase(hombre_imaginario))



from string import ascii_letters
