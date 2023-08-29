def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    letras_validas = {'A', 'C', 'T', 'G'}
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    return True


secuencia = input("Ingrese una secuencia de ADN: ")


if es_secuencia_genoma(secuencia):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")
      