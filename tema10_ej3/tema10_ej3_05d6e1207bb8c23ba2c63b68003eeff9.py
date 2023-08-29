archivo=open("sopa.txt","r")
archivo.close()
def sopaletras(sopa,palabras):    
    return [(palabras[0],[0,0],"diagonal")]
if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))           