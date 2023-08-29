 def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    indice2 = 0

    for i in range(len(secuencia1)):
        if secuencia1[i] == secuencia2[indice2]:
            alineacion += secuencia2[indice2]
            indice2 += 1
        else:
            alineacion += "_"

    alineacion += secuencia2[indice2:]

    return alineacion

# Ejemplo de uso
secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinear_secuencias(secuencia1, secuencia2)
print("El segundo string alineado con el primero es:", resultado)
 