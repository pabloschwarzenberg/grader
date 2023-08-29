def estadisticas_frase(frase):
    import re
    palabras=frase.split(' ')
    fraseNoEspacio= re.sub(r"\s+", "", frase, flags=re.UNICODE).replace(".","")
    palabras2=frase.split()
    nroPalabras=len(palabras2)
    espacios=len(palabras)-1
    totalCaracteres=0
    signosPuntuacion=0
    for m in palabras:
        totalCaracteres=len(frase)
        for l in range(0,len(m)):
            if m[l] == "." or m[l] == "," or m[l] == ";" or m[l] == ":":
                signosPuntuacion+=1
    largoPromedio=len(fraseNoEspacio)/nroPalabras
    return nroPalabras,totalCaracteres,largoPromedio,espacios,signosPuntuacion