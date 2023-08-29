def alinear_secuencias(secuencia1, secuencia2):
    i = 0
    for c in secuencia1:
        if c != secuencia2[i]:
            secuencia2 = secuencia2[:i] + '_' + secuencia2[i:]
        i += 1
    return secuencia2

# Ejemplo de uso
secuencia1 = input("Ingrese la primera secuencia: ")
secuencia2 = input("Ingrese la segunda secuencia: ")
resultado = alinear_secuencias(secuencia1, secuencia2)
print(resultado)
