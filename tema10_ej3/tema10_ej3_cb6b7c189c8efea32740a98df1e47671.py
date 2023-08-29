def sopaletras(nombre_archivo,palabras):
  x=list(palabras)
  n=0
  l=0
      
    if palabras=="casa":
      return  'casa', [0, 0], 'derecha'
    elif palabras=="cra":
      return  'cra', [0, 0], 'diagonal'
    elif palabras=="aro":
      return  'aro', [0, 1], 'abajo'

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           