import random

def ocultar_letras(palabra, cantidad):
    for j in range(0, cantidad):
        sw = True
        while sw:
            i = random.randrange(0,len(palabra))
            if(palabra[i] != "_" or palabra == "_"*len(palabra)):
                palabra = palabra[:i]+"_"+palabra[i+1:]
                sw = False
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    if(palabra_secreta == letra):
        return letra
    for i in range(0,len(palabra_secreta)):
        if(palabra_secreta[i] == letra):
            palabra = palabra[:i]+letra+palabra[i+1:]
    return palabra

if __name__ == "__main__":
    palabras = ["avion", "auto", "camion", "superman", "teclado", "panaderia"]
    palabra = random.choice(palabras)
    intentos = 7
    palabra_oculta = ocultar_letras(palabra, 4)
    fin = True
    while(intentos > 0 and fin):
        print("")
        print("Le quedan",intentos,"intentos")
        print("Adivine la palabra oculta:", palabra_oculta)
        palabra_oculta = revisar_letra(palabra, palabra_oculta, input("Ingrese una letra o la palabra completa: "))
        intentos -= 1
        if(palabra_oculta == palabra):
            print("Felicidades gano!!. La palabra es", palabra_oculta)
            fin = False
        if(intentos == 0):
            print("Perdiste :c")
         