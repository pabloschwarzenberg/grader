#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        print("CONTESTAR")
    elif hora < 14 and numero % 100 == 909:
        print("CONTESTAR")
    elif hora >= 17 and hora <= 19 and str(numero).startswith('877'):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR") 
        
  # Pedir al usuario que ingrese la hora del día y el número de teléfono
hora = int(input("Ingrese la hora del día (0-23): "))
numero = int(input("Ingrese el número de teléfono (8 cifras): "))

# Llamar a la función para determinar si se debe contestar o no
contestar_llamada(hora, numero)