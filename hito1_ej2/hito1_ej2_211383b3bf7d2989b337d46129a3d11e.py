def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] != "909":
        return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19 and not str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Ejemplo 1: Llamada a las 03:30 desde el número 78735653
respuesta1 = contestar_llamada(3, 78735653)
print(respuesta1)  # Resultado esperado: CONTESTAR

# Ejemplo 2: Llamada a las 10:45 desde el número 78735653
respuesta2 = contestar_llamada(10, 78735653)
print(respuesta2)  # Resultado esperado: NO CONTESTAR

# Ejemplo 3: Llamada a las 11:30 desde el número 78735653
respuesta3 = contestar_llamada(11, 78735653)
print(respuesta3)  # Resultado esperado: NO CONTESTAR

# Ejemplo 4: Llamada a las 13:30 desde el número 78735653
respuesta4 = contestar_llamada(13, 78735653)
print(respuesta4)  # Resultado esperado: NO CONTESTAR

# Ejemplo 5: Llamada a las 13:30 desde el número 78735653
respuesta5 = contestar_llamada(13, 78735653)
print(respuesta5)  # Resultado esperado: NO CONTESTAR

# Ejemplo 6: Llamada a las 16:30 desde el número 78735653
respuesta6 = contestar_llamada(16, 78735653)
print(respuesta6)  # Resultado esperado: NO CONTESTAR

# Ejemplo 7: Llamada a las 18:30 desde el número 78735653
respuesta7 = contestar_llamada(18, 78735653)
print(respuesta7)  # Resultado esperado: CONTESTAR

# Ejemplo 8: Llamada a las 18:30 desde el número 87712345
respuesta8 = contestar_llamada(18, 87712345)
print(respuesta8)  # Resultado esperado: NO CONTESTAR

# Ejemplo 9: Llamada a las 20:30 desde el número 78735653
respuesta9 = contestar_llamada(20, 78735653)
print(respuesta9)  # Resultado esperado: NO CONTESTAR
