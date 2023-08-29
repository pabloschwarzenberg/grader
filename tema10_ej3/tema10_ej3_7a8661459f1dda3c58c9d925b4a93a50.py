def sopaletras(nombre_archivo,palabras):
    archivo = open(nombre_archivo,"r")
    
    #verificamos de izquierda a derecha
    salida = []
    for linea in archivo:
        aux = linea.split(' ')
        palabra = ""
        for i in range(0,len(aux)):
            palabra += aux[i][0]
        palabra = palabra.lower()
        for p in palabras:
            if p in palabra:
                tupla = (palabra,[palabra.find(p),palabra.find(p)],'derecha')
                salida.append(tupla)
    archivo.close()
    #verificamos de arriba a abajo
    archivo = open(nombre_archivo,"r")
    lines = archivo.readlines()
    for i in range(0,len(lines[0])-1):
        palabra = ""
        for p in lines:
            aux = linea.split(' ')
            palabra += p[i][0]
        palabra = palabra.lower()
        for p in palabras:
            if p in palabra:
                tupla = (palabra,[palabra.find(p),i-1],'abajo')
                salida.append(tupla)
    archivo.close()
    #buscamos de manera diagonal
    archivo = open(nombre_archivo,"r")
    lines = list(archivo.readlines())
    i = 0
    diagonal = ""
    for linea in lines:
        aux = linea.split(' ')
        diagonal += aux[i][0]
        i += 1
    diagonal = diagonal.lower()
    for palabra in palabras:
        if palabra in diagonal:
            tupla = (palabra,[diagonal.find(palabra),diagonal.find(palabra)],'diagonal')
            salida.append(tupla)
            
    return salida


if __name__=="__main__":
    print(sopaletras("sopa.txt",["cra"]))
    print(sopaletras("sopa.txt", ["aro"]))
    print(sopaletras("sopa.txt", ["casa"]))
    print(sopaletras("sopa.txt",["casa","cra","aro"]))

           