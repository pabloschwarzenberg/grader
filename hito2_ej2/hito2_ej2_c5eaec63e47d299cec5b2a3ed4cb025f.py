def validar_secuencia(secuencia):
    secuencia = secuencia.upper()  # Convertir a mayúsculas para no distinguir entre mayúsculas y minúsculas
    
    for base in secuencia:
        if base not in ['A', 'C', 'T', 'G']:
            return False
    return True

#solicitud
secuencia_genoma = input("Ingrese la secuencia del genoma: ")

#validacion
if validar_secuencia(secuencia_genoma):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      