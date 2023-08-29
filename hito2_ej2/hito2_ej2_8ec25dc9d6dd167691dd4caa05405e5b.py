def es_genoma(secuencia):
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}

    for letra in secuencia:
        if letra not in letras_validas:
            return False

    return True
secuencia = input("Ingrese la secuencia del genoma: ")
if es_genoma(secuencia):
    print("Secuencia correcta. Es un genoma válido.")
else:
    print("Secuencia incorrecta. No es un genoma válido.")