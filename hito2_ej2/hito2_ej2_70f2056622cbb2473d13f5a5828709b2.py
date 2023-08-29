def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()
    letras_permitidas = {'A', 'C', 'T', 'G'}
    for letra in secuencia:
        if letra not in letras_permitidas:
            return False
    return True
secuencia_input = input("Ingrese la secuencia del genoma: ")
if validar_secuencia_genoma(secuencia_input):
    print("Secuencia correcta: representa un genoma")
else:
    print("Secuencia incorrecta: no representa un genoma")