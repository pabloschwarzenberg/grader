def jerigonzo(string):
    #Definimos esta tupla para comparar de manera rC!pida
    #si serC! necesario agregar una p.
    vocales = ("a","e","i","o","u")
    ret = ""
    #Recorremos el texto letra por letra, para ir aC1adiC)ndola
    #a nuestro string ret
    for letra in string:
        #Sabemos que la letra se aC1ade si o si al texto, por
        #lo que la sumamos
        ret += letra
        #Luego, si la letra que aC1adimos fue una vocal, le agregamos
        #una p, seguida de la misma vocal
        if letra in vocales:
            ret += "p" + letra
        #Revisamos la siguiente letra
    #Una vez recorrido todo el string, lo retornamos, se pide
    #retornar, no imprimir.
    return ret

if __name__ == "__main__":
    print(jerigonzo("estamos programando"))
