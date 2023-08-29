#Jerigonzo
def jerigonzo(string):
    nuevoTexto= ""
    for i in range(len(string)):
        nuevoTexto= nuevoTexto + string[i]
        if string[i] in "aeiouAEIOU":
            nuevoTexto= nuevoTexto + "p" + string[i]        
    return nuevoTexto
