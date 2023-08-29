def validar_secuencia_genoma(secuencia):
    secuencia = secuencia.upper()  
    
    for letra in secuencia:
        if letra not in ['A', 'C', 'T', 'G']:
            return False
    
    return True

secuencia = input("Ingrese la secuencia de ADN: ")

if validar_secuencia_genoma(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      