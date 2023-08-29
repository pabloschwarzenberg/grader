def alinear_secuencias(secuencia1, secuencia2):
    aligned_sequence = ""
    index = 0

    for char in secuencia1:
        if char == secuencia2[index]:
            aligned_sequence += secuencia2[index]
            index += 1
        else:
            aligned_sequence += "_"

    aligned_sequence += secuencia2[index:]

    return aligned_sequence

if __name__ == "__main__":
    secuencia1 = input("Ingrese la primera secuencia: ")
    secuencia2 = input("Ingrese la segunda secuencia: ")

    aligned_sequence = alinear_secuencias(secuencia1, secuencia2)
    print(aligned_sequence)
     