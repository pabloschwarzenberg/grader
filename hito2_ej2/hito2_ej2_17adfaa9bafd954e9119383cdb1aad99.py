def validar_secuencia(secuencia):
    
    secuencia = secuencia.upper()
   
    for base in secuencia:
        if base not in ['A', 'C', 'T', 'G']:
            return False

    return True

secuencia_input = input("Ingrese la secuencia de ADN: ")

if validar_secuencia(secuencia_input):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")