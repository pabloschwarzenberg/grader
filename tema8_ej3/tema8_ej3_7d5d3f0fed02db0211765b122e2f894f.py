def estadisticas_frase(s):
    cont_palabras = 0
    cont_chars = 0
    cont_espa = 0
    cont_punt = 0
    lin_no_vacias = s.splitlines()
    list = []
    larg_prom = 0
    palabras = s.split(" ")
    for elemento in palabras:
        if elemento == "\n":
            elemento.replace("\n", " ")
    for oracion in lin_no_vacias:
        if oracion == "":
            lin_no_vacias.remove("")
    cont_palabras += len(lin_no_vacias)
    for char in s:
        cont_chars += 1
        if char == " ":
            cont_espa += 1
            cont_palabras += 1
        elif char == "." or char == "," or char == ":" or char == ";":
            cont_punt += 1
    for x in lin_no_vacias:
        list.append(x.strip("..."))
    for a in list:
        a = str(a)
        b = a.split(" ")
        for elm in b:
            larg_prom += len(elm)
    larg_prom = larg_prom / cont_palabras
    return cont_palabras, cont_chars, larg_prom, cont_espa, cont_punt