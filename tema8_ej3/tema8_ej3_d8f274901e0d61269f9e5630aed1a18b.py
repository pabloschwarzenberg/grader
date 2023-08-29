imaginary_man = """

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



def estadisticas_frase(firstfrase):

  abcdario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","í","é","ó","ú"]
  firstfrase = firstfrase.lower()
  acentuacion = [",",";",".",":","¿","?","!","¡"]

  i__x = 0 + 0

  e__x = 0 + 0

  x__i = 0 + 0

  x__k = 0 + 0

  x__x = 0 + 0
#............................................................................................................................................
  for c in firstfrase:

    if c in abcdario and firstfrase[i__x+1] not in abcdario:
      x__x += 1

    if c in abcdario:
      x__k += 1

    if c in acentuacion:
      x__i += 1

    if c not in acentuacion and c not in abcdario:
      e__x += 1
    i__x += 1
#............................................................................................................................................
  secondfrase=list(firstfrase)
  newword=len(secondfrase)
  
  e__xnumber2=0
  for l in secondfrase:
    if l==" ":
      e__xnumber2+=1
  x__k_x__x = x__k/x__x
  return x__x,newword,x__k_x__x,e__xnumber2,x__i

#............................................................................................................................................

if __name__ == "__main__":

  print(estadisticas_frase(imaginary_man))
  
                                                                                                                                                                                                                                                   #━━━━━-╮
                                                                                                                                                                                                                                                 #╰┃ ┣▇━▇}
                                                                                                                                                                                                                                                 # ┃ ┃  ╰━▅╮
                                                                                                                                                                                                                                                   #╰┳╯ ╰━━┳╯F A S I L I T O
                                                                                                                                                                                                                                                    #╰╮ ┳━━╯ E L
                                                                                                                                                                                                                                                    #▔▋ ╰╮╭━╮ T U T O R I A L
                                                                                                                                                                                                                                                  #╱▔╲▋╰━┻┻╮╲╱▔▔▔╲
                                                                                                                                                                                                                                                #▏  ▔▔▔▔▔▔▔  O O┃
                                                                                                                                                                                                                                                     #╲╱▔╲▂▂▂▂╱▔╲▂▂▂╱
                                                                                                                                                                                                                                                      #▏╳▕▇▇▕ ▏╳▕▇▇


         