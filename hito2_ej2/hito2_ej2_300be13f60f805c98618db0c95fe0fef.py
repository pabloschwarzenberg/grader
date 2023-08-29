def es_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas
    letras_validas = {'A', 'C', 'T', 'G'}
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    return True

entrada = input("Ingrese una secuencia: ")
if es_secuencia_genoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      