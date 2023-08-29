def genoma(secuencia):
    secuencia=list(secuencia)
    i=0
    while i<len(secuencia):
        letra=secuencia[i]
        letra=str(letra)
        if letra!="A" or letra!="C" or letra!="T" or letra!="G":
            return (print("secuencia incorrecta"))
        else:
            i+=1
    return (print("secuencia correcta"))
   
secuencia=input("Ingresa secuencia: ")
genoma(secuencia)