#Contestador de celular
def contestar_llamada(numero, hora):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora < 7:
        return True
    
    # Verificar si la llamada ocurre antes de las 14:00
    if hora < 14:
        # Verificar si el número termina en 909
        if numero % 1000 == 909:
            return True
        else:
            return False
    
    # Verificar si la llamada ocurre entre 17:00 y 19:00
    if hora >= 17 and hora < 19:
        # Verificar si el número comienza por 877
        if numero // 100000 == 877:
            return False
    
    # No contestar la llamada en cualquier otro caso
    return False

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese el número telefónico (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada utilizando la función contestar_llamada
if contestar_llamada(numero, hora):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")