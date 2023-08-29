def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Se contesta siempre entre las 00:00 y las 07:00
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).endswith("877"):
        return "NO CONTESTAR"
    else: 
        return "NO CONTESTAR"
    
numero = int(input("Ingrese el número de celular (8 dígitos): "))
hora = float(input("Ingrese la hora (0-23): "))


# Llamar a la función y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)

# Llamar a la función y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)
# Llamar a la función y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)