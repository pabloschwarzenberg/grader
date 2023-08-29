def alinear_secuencias(s1, s2):
    resultado = ''
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            resultado += s2[j]
            i += 1
            j += 1
        else:
            resultado += '_'
            i += 1
    while i < len(s1):
        resultado += '_'
        i += 1
    while j < len(s2):
        resultado += s2[j]
        j += 1
    return resultado

s1 = input('Ingresa la primera secuencia: ')
s2 = input('Ingresa la segunda secuencia: ')
resultado = alinear_secuencias(s1, s2)
print(resultado)
