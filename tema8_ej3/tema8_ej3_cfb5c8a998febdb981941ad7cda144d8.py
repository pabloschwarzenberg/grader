def estadisticas_frase(s):
    s1 = s.split(" ")
    numeropalabras = len(s1)
    caracteres=[]
    for i in s:
        caracteres.append(i)
    numerocaracteres = len(caracteres)
    espacios = s.count(" ")
    return numeropalabras,numerocaracteres,espacios         