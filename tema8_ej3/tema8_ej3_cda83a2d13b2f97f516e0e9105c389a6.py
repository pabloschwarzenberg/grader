def estadisticas_frase(s) :
    numero_caracteres_puntuacion = s.count(",") + s.count(".") + s.count(":") + s.count(";")
    a = s.strip(",")
    b = a.strip(".")
    c = b.strip(":")
    d = c.strip(";")
    lista_palabras = d.split()
    numero_palabras = len(lista_palabras)
    numero_caracteres = len(s)
    print(lista_palabras)
    largo_palabras = 0
    for palabra in lista_palabras :
        largo_palabras += len(palabra)
    print(largo_palabras)
    promedio_largos = largo_palabras / numero_palabras
    numero_espacios = s.count(" ")
    return numero_palabras,numero_caracteres,promedio_largos,numero_espacios,numero_caracteres_puntuacion


         