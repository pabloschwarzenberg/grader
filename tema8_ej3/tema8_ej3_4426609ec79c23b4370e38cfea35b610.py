def estadisticas_frase(frase):

    i = 0
    largo = 0
    frase1 = frase.replace(".","")
    palabras = frase1.split()
    
    texto = frase.strip()

    texto = texto.replace(" ","").replace(".","")
    print(texto)
    
    espacio = 0
    caracter = 0
    punto = 0

    for c in frase:
        

        if c == " ":
            espacio = espacio + 1
         

        if c == ".":
            punto = punto + 1

        if c != " " or c != "." or c != "" :
            
            caracter = caracter + 1
        

    palabra = 0
    while i < len(palabras):
        palabra = palabra + len(palabras[i])
        i = i + 1
    promedio = palabra / len(palabras)
    
    return len(palabras),caracter,promedio,espacio,punto       