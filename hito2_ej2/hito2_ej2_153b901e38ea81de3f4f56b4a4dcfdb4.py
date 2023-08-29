def cod(c):
    nuevoc=c.upper()
    for letra in nuevoc:
        if letra!="A" and letra!="C" and letra!="G" and letra!="T": 
            no="secuencia incorrecta"
            return no
    si="secuencia correcta"
    return si
codigo=input("Ingrese codigo")
print(cod(codigo))
 