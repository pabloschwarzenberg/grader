def validar_genoma(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas
    letras_validas = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    
    return True
entrada = input("Ingrese la secuencia de ADN: ")

if validar_genoma(entrada):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")