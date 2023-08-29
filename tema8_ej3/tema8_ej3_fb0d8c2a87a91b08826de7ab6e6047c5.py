def estadisticas_frase(frase):
    largo=len(frase)
    x=frase.split(" ")
    numerodepalabras=len(x)
    s=list(frase)
    numerodecaracteres=len(frase)
    numerodeespacio=0
    numerodepuntuacion=0
    g = 0
    t = 1
    while g<largo:
        if s[g]==" ":
            if s[g] == " " and s[t] == " ":
                numerodeespacio = numerodeespacio 
                t +=1
                g +=1
            else:
                numerodeespacio=numerodeespacio + 1
                g +=1
                t +=1
        elif s[g]==".":
            numerodepuntuacion=numerodepuntuacion + 1
            g +=1
            t +=1
        else:
            numerodecaracteres = numerodecaracteres + 1
            g +=1
            t +=1
    numerodecaracteres = numerodecaracteres - numerodeespacio - numerodepuntuacion
    numerodeletra=numerodecaracteres-numerodeespacio
    promedio=numerodeletra/numerodepalabras
    promedio=round(promedio,2)
    return(numerodepalabras,numerodecaracteres,promedio,numerodeespacio,numerodepuntuacion)

