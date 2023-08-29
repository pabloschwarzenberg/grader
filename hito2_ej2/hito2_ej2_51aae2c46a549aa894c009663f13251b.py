# Validar Secuencias de ADN
secuencia = input("Ingrese secuencia de ADN: ")

secuencia = secuencia.upper()

if((secuencia[0] == 'A') and (secuencia[1] == 'C') and (secuencia[2] == 'T') and (secuencia[3] == 'G')):
    print("\nSecuencia correcta.")
else:
    print("\nSecuencia incorrecta.")