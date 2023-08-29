def sopaletras(nombre_archivo,palabras):
    with open(nombre_archivo, "r") as archivo:
        soup = []
        print(soup)
        for line in archivo.readlines():
            soup.append(line.strip().split(" "))
        print(soup)

    for palabra in palabras:
        palabralist = list(palabra.upper())
        print(palabralist)

        for line in soup:
            if line == palabralist:
                return [(palabras[palabras.index(palabra)],[soup.index(line),0],"derecha")]