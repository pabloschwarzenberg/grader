def alinear_secuencias(seq1, seq2):
    alineacion = ""
    indice_seq2 = 0
    
    for caracter in seq1:
        if caracter == seq2[indice_seq2]:
            alineacion += seq2[indice_seq2]
            indice_seq2 += 1
        else:
            alineacion += "_"
    
    alineacion += seq2[indice_seq2:]
    return alineacion


# Obtener la entrada del usuario
seq1 = input("Ingrese la primera secuencia de ADN: ")
seq2 = input("Ingrese la segunda secuencia de ADN: ")

# Realizar el alineamiento
resultado = alinear_secuencias(seq1, seq2)

# Imprimir el resultado
print(resultado)

