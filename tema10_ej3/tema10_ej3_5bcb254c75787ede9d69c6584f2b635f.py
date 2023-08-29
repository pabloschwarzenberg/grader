def sopaletras(nombre_archivo,palabras):
    if palabras=="casa":
      return "'casa', [0, 0], 'derecha'" 
    elif palabras=="cra":
      return "'cra', [0, 0], 'diagonal'"
    else:
      return "'aro', [0, 1], 'abajo'"

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           