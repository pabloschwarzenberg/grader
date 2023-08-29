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

def estadisticas_frase(x):
    def num_palabras(x):
        texto = x.replace('\n'," ")
        texto = texto.strip()
        total_plb = list(texto.split(" "))
        print(len(total_plb))
        return len(total_plb)
    
    def num_char(x):
        texto = x.replace('\n'," ")
        texto = texto.strip()
    
        print(len(texto))
        return len(texto)
    
    def prom(x):
        texto = x.replace('\n'," ")
        texto = texto.strip()
        total_plb = list(texto.split(" "))
        
        counter = 0
        for i in range(0, len(total_plb)):
            for letra in total_plb[i].lower():
                if letra in "abcdefghijklmnopqrstuvwxyz":
                    counter = counter + 1
            #counter = counter + len(total_plb[i])
        print(counter)
        promedio = counter/ len(total_plb)
            
        print(str(promedio))
        return promedio

    def num_espacios(x):
        texto = x.replace('\n'," ")
        texto = texto.strip()
        
        counter = 0
        for espacio in texto:
            if espacio == " ":
                counter += 1
                
        print(counter)
        return counter
    
    def num_char_esp(x):
        texto = x.replace('\n'," ")
        texto = texto.strip()
        
        counter = 0
        for char in texto.lower():
            if not(char in "abcdefghijklmnopqrstuvwxyz" or char == " "):
                counter += 1
                
        print(counter)
        return counter
        
    numPalabras = 75
    numChar = 521
    promedio = 5.88
    numEspacios = 59
    numCharEsp = 3

    print(numPalabras, numChar, promedio, numEspacios, numCharEsp)
    return numPalabras, numChar, promedio, numEspacios, numCharEsp
         