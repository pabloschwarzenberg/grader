cadenaPalabras = 'El hombre imaginario vive en una mansión imaginaria rodeada de árboles imaginarios a la orilla de un río imaginario De los muros que son imaginarios penden antiguos cuadros imaginarios irreparables grietas imaginarias que representan hechos imaginarios ocurridos en mundos imaginarios en lugares y tiempos imaginarios Todas las tardes tardes imaginarias sube las escaleras imaginarias y se asoma al balcón imaginario a mirar el paisaje imaginario que consiste en un valle imaginario circundado de cerros imaginarios...'


listaPalabras = cadenaPalabras.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(list(zip(listaPalabras, frecuenciaPalab))))
         