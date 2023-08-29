def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    l= []
    for i in range(0, len(palabras)):
        l.append([ palabras[i], verifica(nombre_archivo, palabras[i])])    
    archivo.close()
    return l

if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

def verifica(nombre_archivo, palabra):
    archivo=open(nombre_archivo,"r")
    l=[]
    status = "nada"
    salir= False
    largo= len(palabra)
    for i in range(0, 3):
        for j in range(0, 4):
            if palabra[0] == archivo[i,j]:
                ubicacion=[i, j]
                a=0
                while j <= 3 and archivo[i,j] == palabra[a]:
                    j= j+1
                    a= a+1
                if a == largo - 1:
                    status = "derecha"
                    salir = True
                    break
                else:
                    b=0
                    while i<= 2 and archivo[i,j]== palabra[b]:
                        i= i+1
                        b= b+1
                    if b == len(palabra) - 1:
                        status = "abajo"
                        salir = True
                        break
                    else:
                        c=0
                        while archivo[i,j]== palabra[c] and i<= 2 and j<=3:
                            i=i+1
                            j=j+1
                            c=c+1
                        if c + 1 == len(palabra):
                            status = "diagonal"
                            salir = True
                            break
        if salir:
            break
        l.append(ubicacion, status)
        archivo.close()
    return l
    


           