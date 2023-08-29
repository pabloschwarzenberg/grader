def rot13(palabra):
    import string
    palabral=list(palabra)
    Codigo=''
    for i in range (len(palabral)):
        if palabral[i] in string.ascii_uppercase:
            LetrasGrandes_iniciales=list(string.ascii_uppercase[0:13])
            LetrasGrandes_finales=list(string.ascii_uppercase[13:len(string.ascii_uppercase)])
            if palabral[i] in LetrasGrandes_iniciales:
                for t in range(len(LetrasGrandes_iniciales)):
                    if LetrasGrandes_iniciales[t]==palabral[i]:
                        palabral[i]=LetrasGrandes_finales[t]
            elif palabral[i] in LetrasGrandes_finales:
                for t in range (len(LetrasGrandes_finales)):
                    if LetrasGrandes_finales[t]==palabral[i]:
                        palabral[i]=LetrasGrandes_iniciales[t]
            Codigo=Codigo+palabral[i]
    for i in range (len(palabral)):
        if palabral[i] in string.ascii_lowercase:
            Letraschicas_iniciales=list(string.ascii_lowercase[0:13])
            Letraschicas_finales=list(string.ascii_lowercase[13:len(string.ascii_lowercase)])
            if palabral[i] in Letraschicas_iniciales:
                for t in range(len(Letraschicas_iniciales)):
                    if Letraschicas_iniciales[t]==palabral[i]:
                        palabral[i]=Letraschicas_finales[t]
            elif palabral[i] in Letraschicas_finales:
                for t in range (len(Letraschicas_finales)):
                    if Letraschicas_finales[t]==palabral[i]:
                        palabral[i]=Letraschicas_iniciales[t]
            Codigo=Codigo+palabral[i]
    return Codigo

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           