def estadisticas_frase(s):
    caracteres = len(s)
    n_espacios  = 0
    n_puntiacion = 0
    c = None
    for i in s:
        if c == " ":
            n_espacios += 1
        if c == ".":
            n_puntiacion += 1
    s = s.strip(".")
    palabras = len(s.split())
    
    prom_letras = list(s.split())
    s = 0
    suma = 0 
    for x in range(palabras):
        s = len(prom_letras[x])
        x = x + 1
        suma += s
    return palabras, caracteres, suma / palabras, n_espacios, n_puntiacion      