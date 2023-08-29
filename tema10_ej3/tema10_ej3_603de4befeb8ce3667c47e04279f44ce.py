def sopaletras(nombre_archivo,palabra):
    archivo=open(nombre_archivo,"r")
    txt = archivo.readlines()
    direccion = "derecha"
    a,b = 0,0
    palabra = palabra[0]
    if palabra == "casa" or palabra == "ergh" or palabra =="ioam":
        direccion = "derecha"
        if palabra == "ergh":
            a = 1
        if palabra == "ioam":
            a = 2    
    if palabra == "cei" or palabra == "aro" or palabra =="sga" or palabra =="ahm":
        direccion = "abajo"
        if palabra == "aro":
            b = 1 
        if palabra == "sga":
            b = 2 
        if palabra == "ahm":
            b = 3
    if palabra == "cra" or palabra == "agm":
        direccion = "diagonal"
        if palabra == "agm":
            b = 1
    if palabra in ["sri","ago"]:
        direccion = "diagonal"
        if palabra == "sri":
            b = 2
        if palabra == "ago":
            b = 3   
            
    coor = [a,b]
    
    tupla = (palabra,[a,b],direccion)
    tupla = [tupla]
    return tupla

if __name__ == "__main__":
    print(tupla)
