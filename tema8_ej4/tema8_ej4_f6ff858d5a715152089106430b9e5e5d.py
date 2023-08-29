def rot13(palabra):
    resultado = ""
    for i in palabra:

        if str(i) == "a":
            resultado = resultado + "n"
        
        elif str(i) == "b":
            resultado = resultado + "o"

        elif str(i) == "c":
            resultado = resultado +  "p"

        elif str(i) == "d":
            resultado = resultado +  "q"

        elif str(i) == "e":
            resultado = resultado + "r"

        elif str(i) == "f":
            resultado = resultado + "s"

        elif str(i) == "g":
            resultado = resultado + "t"

        elif str(i) == "h":
            resultado = resultado + "u"

        elif str(i) == "i":
            resultado = resultado + "v"

        elif str(i) == "j":
            resultado = resultado + "w"

        elif str(i) == "k":
            resultado = resultado + "x"

        elif str(i) == "l":
            resultado = resultado + "y"

        elif str(i) == "m":
            resultado = resultado + "z"

        elif str(i) == "n":
            resultado = resultado + "a"

        elif str(i) == "o":
            resultado = resultado + "b"

        elif str(i) == "p":
            resultado = resultado + "c"

        elif str(i) == "q":
            resultado = resultado + "d"

        elif str(i) == "r":
            resultado = resultado + "e"

        elif str(i) == "s":
            resultado = resultado + "f"

        elif str(i) == "t":
            resultado = resultado + "g"

        elif str(i) == "u":
            resultado = resultado + "h"

        elif str(i) == "v":
            resultado = resultado + "i"

        elif str(i) == "w":
            resultado = resultado + "j"

        elif str(i) == "x":
            resultado = resultado + "k"

        elif str(i) == "y":
            resultado = resultado + "l"

        elif str(i) == "z":
            resultado = resultado + "m"

    return resultado

if __name__=="__main__":
    palabra = input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado = rot13(palabra)
    print("El resultado es: ",resultado)