def validar_secuencia(secuencia):
    secuencia = secuencia.upper() # Convertimos todo a mayúsculas para no distinguir entre mayúsculas y minúsculas
    validos = {'A', 'C', 'T', 'G'} # Set con las letras válidas
    for letra in secuencia:
        if letra not in validos: # Si alguna letra no es válida, retornamos False
            return False
    return True

secuencia = input("Ingrese una secuencia de ADN: ")
if validar_secuencia(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")