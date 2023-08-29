def ADN (a):
    if ("a" and "c" and "t" and "g") and ("A" and "C" and "T" and "G") in a :
        return("secuencia correcta")
    else:
        return("secuenia incorrecta")
i=input("ingrese la secuencia: ")
salida= ADN(i)
print(salida)