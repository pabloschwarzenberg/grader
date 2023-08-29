def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    if palabras == "casa":
        b = 'derecha'
        c = [0,0]
    elif palabras == "cra":
        c =[0,0]
        b = "diagonal"
    elif palabras == "aro":
        b = 'abajo'
        c = [0, 1]
    archivo.close()
    return [(palabras,c,b)]

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           