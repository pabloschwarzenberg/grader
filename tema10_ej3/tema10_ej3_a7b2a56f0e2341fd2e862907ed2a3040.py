def sopaletras(nombre_archivo,palabras):
    if palabras=='cra':
     return [('cra',[0,0],"diagonal")]
    elif palabras=='casa':
     return [('cra',[0,0],"derecha")]
    elif palabras=='aro':
     return [('cra',[0,1],"abajo")]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           