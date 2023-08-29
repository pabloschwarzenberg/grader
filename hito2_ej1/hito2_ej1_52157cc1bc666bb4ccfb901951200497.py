def alinear_secuencias(secuencia1, secuencia2):
    alineacion = ""
    index_secuencia2 = 0
    
    for caracter in secuencia1:
        if index_secuencia2 < len(secuencia2) and caracter == secuencia2[index_secuencia2]:
            alineacion += secuencia2[index_secuencia2]
            index_secuencia2 += 1
        else:
            alineacion += "_"
    
    alineacion += secuencia2[index_secuencia2:]
    
    return alineacion

secuencia1 = input("Ingrese la primera secuencia de ADN: ")
secuencia2 = input("Ingrese la segunda secuencia de ADN: ")

resultado = alinear_secuencias(secuencia1, secuencia2)

print("Secuencia alineada:")
print(resultado)
   