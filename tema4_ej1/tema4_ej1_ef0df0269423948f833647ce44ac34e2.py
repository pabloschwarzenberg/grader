import random

def ocultar_letras(palabra,cantidad):
    contador1 = 0
    while contador1 < cantidad:
        a = random.randrange(0,len(palabra))
        if palabra[a] != "_":
            palabra = palabra [:a] + "_" + palabra[a+1:]
            contador1 = contador1 + 1
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    contador2 = 0

    while contador2 < len (palabra_secreta):
        if palabra_secreta [contador2] == letra:
           palabra = palabra[:contador2] + letra + palabra[contador2 + 1:]
        contador2 = contador2 + 1

    return palabra
    return palabra

if __name__ == "__main__":
    x = random.randrange(0,7)
    listado_palabras =  ["mesa","silla", "florero", "cuadro", "planta", "televisor", "sillon"]
    palabra = ocultar_letras(listado_palabras[x], random.randrange(1,len (listado_palabras[x])))
    y = 0

    while y < 7:
        ingreso = str(input("Ingrese palabra o letra: "))
        if len (ingreso) > 1:
            if ingreso == listado_palabras [x]:
                print ("Econtraste La Palabra, Felicitaciones")
                y = 7
            else:
                print ("Fallaste, No Es La Palabra")
                print (palabra)
                y = y + 1

        else:
            z = revisar_letra(listado_palabras [x], palabra, ingreso)
            palabra = z
            if palabra == listado_palabras [x]:
                print ("Econtraste La Palabra, Felicitaciones")
                print(palabra)
                y = 7
            else:
                print (palabra)
                y = y + 1
    if palabra != listado_palabras[x]:
        print("Fallaste, No Es La Palabra")
    
    pass
         