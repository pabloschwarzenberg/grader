def estadisticas_frase(frase):
    cp = 0
    d = 0
    pm = 0
    ne = 0
    sp = 0
    for i in frase :
        if i != " " :
            d += 1
        elif i == " " :
            cp += 1
            ne += 1
        elif i == len(frase) - 1 :
            cp += 1
        elif i == "." or i == "," or i == ":" or i == ";" or i == "(" or i == ")" :
            sp += 1
            d -= 1
        pm += d
  return cp,len(frase),pm/len(frase),ne,sp