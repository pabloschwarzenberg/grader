def rot13(palabra):
    lista = list(palabra)
    i = 0
    x = len(lista)
    while i < x:
        if lista[i] == "a":
            lista[i] = "n"
            i = i + 1
            
        elif lista[i] == "b":
            lista[i] = "o"
            i = i + 1
            
        elif lista[i] == "c":
            lista[i] = "p"
            i = i + 1
            
        elif lista[i] == "d":
            lista[i] = "q"
            i = i + 1
            
        elif lista[i] == "e":
            lista[i] = "r"
            i = i + 1
            
        elif lista[i] == "f":
            lista[i] = "s"
            i = i + 1
            
        elif lista[i] == "g":
            lista[i] = "t"
            i = i + 1
            
        elif lista[i] == "h":
            lista[i] = "u"
            i = i + 1
            
        elif lista[i] == "i":
            lista[i] = "v"
            i = i + 1
            
        elif lista[i] == "j":
            lista[i] = "w"
            i = i + 1
            
        elif lista[i] == "k":
            lista[i] = "x"
            i = i + 1
            
        elif lista[i] == "l":
            lista[i] = "y"
            i = i + 1
            
        elif lista[i] == "m":
            lista[i] = "z"
            i = i + 1
            
        elif lista[i] == "n":
            lista[i] = "a"
            i = i + 1
            
        elif lista[i] == "o":
            lista[i] = "b"
            i = i + 1
            
        elif lista[i] == "p":
            lista[i] = "c"
            i = i + 1
            
        elif lista[i] == "q":
            lista[i] = "d"
            i = i + 1
            
        elif lista[i] == "r":
            lista[i] = "e"
            i = i + 1
            
        elif lista[i] == "s":
            lista[i] = "f"
            i = i + 1
            
        elif lista[i] == "t":
            lista[i] = "g"
            i = i + 1
            
        elif lista[i] == "u":
            lista[i] = "h"
            i = i + 1
            
        elif lista[i] == "v":
            lista[i] = "i"
            i = i + 1
            
        elif lista[i] == "w":
            lista[i] = "j"
            i = i + 1
            
        elif lista[i] == "x":
            lista[i] = "k"
            i = i + 1
            
        elif lista[i] == "y":
            lista[i] = "l"
            i = i + 1
            
        elif lista[i] == "z":
            lista[i] = "m"
            i = i + 1
            
    linea = ""
    for celda in lista:
        linea = linea + str(celda)
    return linea
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           