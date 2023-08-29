hombre_imaginario = """
El hombre imaginario
vive en una mansión imaginaria
rodeada de árboles imaginarios
a la orilla de un río imaginario

De los muros que son imaginarios
penden antiguos cuadros imaginarios
irreparables grietas imaginarias
que representan hechos imaginarios
ocurridos en mundos imaginarios
en lugares y tiempos imaginarios

Todas las tardes tardes imaginarias
sube las escaleras imaginarias
y se asoma al balcón imaginario
a mirar el paisaje imaginario
que consiste en un valle imaginario
circundado de cerros imaginarios..."""

def estadisticas_frase(s):  
#numero de palabras
    palabras_separadas = s.split(" ")
    numero_palabras = len(palabras_separadas)

#numero total de caracteres EN CASO QUE "CARACTERES" SE REFIERA A CUALQUIER CARACTER
#numero caracteres de puntuacion

    letras_español = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista_largo_palabras = []
    palabra_elegida = 0

    suma_caracteres = 0
    suma_caracteres_puntuacion = 0
    
    while palabra_elegida < numero_palabras:
        lista_palabra_elegida = list(palabras_separadas[palabra_elegida])

        letra_elegida = 0
        largo_palabra = 0
        while letra_elegida < len(lista_palabra_elegida):
            
            #Se vuelve a minuscula la letra elegida, para que no ocurran errores al compararla con las letras de letras_español
            letra = lista_palabra_elegida[letra_elegida]
            letra = letra.lower()

            #se considera para el largo de la palabra solo si es una letra española, esto para no contar mal el largo de "imaginarios..."
            if letra in letras_español:
                largo_palabra = largo_palabra + 1
                suma_caracteres = suma_caracteres + 1
                    
            #Esto es en caso de que el elemento sea un caracter de puntuacion (. , ; etc), se debe sumar a suma_caracteres_puntuacion y a suma_caracteres
            elif letra == ".":
                suma_caracteres = suma_caracteres + 1
                suma_caracteres_puntuacion = suma_caracteres_puntuacion + 1

            letra_elegida = letra_elegida + 1

        #Se añade el largo de la palabra analizada a la lista de los largos de las palabras   
        lista_largo_palabras.append(largo_palabra)
        
        palabra_elegida = palabra_elegida + 1
            
        
#largo promedio de las palabras (las palabras con ... no consideran estos puntos para su largo)
        
    #Se suma cada elemento de lista_largo_palabras y se divide en el total de elementos de esta lista
    elemento = 0
    suma_largos = 0
    while elemento < len(lista_largo_palabras):
        suma_largos = suma_largos + lista_largo_palabras[elemento]
        elemento = elemento + 1

    largo_promedio_palabras = suma_largos / len(lista_largo_palabras)
    largo_promedio_palabras = round(largo_promedio_palabras,4)
        
#numero de espacios
    
    #El número de espacios en un texto bien escrito debería tener espacios solo entre palabras, no antes de la primera ni despues de la ultima palabra,
    #tambien, tampoco deberían existir espacios dobles "  "
    numero_espacios = numero_palabras - 1

    return(numero_palabras, suma_caracteres, largo_promedio_palabras, numero_espacios, suma_caracteres_puntuacion)

#EJECUCION