#Contestador de celular
def contestar_llamada(numero, hora):
    # Regla 1: Llamada entre 00:00 y 07:00
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    
    # Regla 2: Llamada antes de las 14:00, excepto si termina en 909
    if hora < 14 and numero % 1000 != 909:
        return "NO CONTESTAR"
    
    # Regla 3: Llamada entre 17:00 y 19:00, excepto si comienza por 877
    if hora >= 17 and hora < 19 and numero // 100000 == 877:
        return "NO CONTESTAR"
    
    # Regla 4: Llamada después de las 19:00
    if hora >= 19:
        return "NO CONTESTAR"
    
    # Si no se cumple ninguna de las reglas anteriores, contestar la llamada
    return "CONTESTAR"

# Solicitar número de teléfono y hora al usuario
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir resultado
print("Resultado:", resultado)




      