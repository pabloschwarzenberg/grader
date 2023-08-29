def validar_genoma(secuencia):
    secuencia = secuencia.upper()
    letras_permitidas = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in letras_permitidas:
            return False
    
    return True

entrada = input("Introduce la secuencia de ADN: ")
if validar_genoma(entrada):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
