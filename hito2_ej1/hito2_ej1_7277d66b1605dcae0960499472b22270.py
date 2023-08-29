def alinear_secuencias(secuencia1, secuencia2):
    secuencia_alineada = ""

    i = 0
    for base in secuencia1:
        if i < len(secuencia2) and secuencia2[i] == base:
            secuencia_alineada += secuencia2[i]
            i += 1
        else:
            secuencia_alineada += "_"

    secuencia_alineada += secuencia2[i:]

    return secuencia_alineada

# Ejemplo de uso
secuencia1_input = input("Ingrese la primera secuencia de ADN: ")
secuencia2_input = input("Ingrese la segunda secuencia de ADN: ")

secuencia_alineada = alinear_secuencias(secuencia1_input, secuencia2_input)

print("Segunda secuencia alineada:")
print(secuencia_alineada)
