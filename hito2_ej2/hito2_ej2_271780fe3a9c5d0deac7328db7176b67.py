def validar_gen(secuencia):
    secuencia = secuencia.upper() 
    letras_validas = {'A', 'C', 'T', 'G'}
    
    for letra in secuencia:
        if letra not in letras_validas:
            return False
    
    return True

secuencia = input("Ingrese la secuencia de ADN: ")

if validar_gen(secuencia):
    print("la secuencia es correcta")
else:
    print("la secuencia es incorrecta")
    