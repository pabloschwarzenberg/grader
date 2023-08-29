def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    j = 0

    for i in range(len(secuencia1)):
        if j < len(secuencia2) and secuencia1[i] == secuencia2[j]:
            alineacion += secuencia2[j]
            j += 1
        else:
            alineacion += "_"

    while j < len(secuencia2):
        alineacion += secuencia2[j]
        j += 1

    return alineacion

secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")

resultado = alinear_secuencias(secuencia1, secuencia2)

print(resultado)

    
   