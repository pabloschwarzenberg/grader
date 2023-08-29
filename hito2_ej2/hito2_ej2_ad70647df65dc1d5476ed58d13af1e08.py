def validar_secuencia(secuencia):
    bases_validas = {'A', 'C', 'T', 'G'}
    secuencia = secuencia.upper()

    for base in secuencia:
        if base not in bases_validas:
            return False

    return True


# Obtener la secuencia del usuario
secuencia = input("Ingrese la secuencia del genoma: ")

# Validar la secuencia
if validar_secuencia(secuencia):
    print("Secuencia correcta. Es compatible con un genoma.")
else:
    print("Secuencia incorrecta. No es compatible con un genoma.")
      