def contestar_celular(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00
    elif hora < 14 and (numero % 1000) == 909:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora < 19 and numero >= 87700000 and numero < 87800000:
        return "CONTESTAR"  # Llamada durante la tarde y número comienza por 877
    else:
        return "NO CONTESTAR"  # Resto de los casos

# Obtener la hora y el número de celular del usuario
hora = int(input("Ingrese la hora (formato de 24 horas): "))
numero = int(input("Ingrese el número de celular: "))

# Verificar si contestar o no
respuesta = contestar_celular(hora, numero)

# Mostrar el resultado
print(respuesta)