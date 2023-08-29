def validar_secuencia(secuencia):
    secuencia = secuencia.upper() 
    
    for nucleotido in secuencia:
        if nucleotido not in 'ACTG':
            return False
    
    return True

secuencia = input("Ingrese la secuencia del genoma: ")

if validar_secuencia(secuencia):
    print("Secuencia correcta.")
else:
    print("Secuencia incorrecta.")