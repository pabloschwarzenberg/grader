def contestar_o_no(hora, telefono):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and (telefono % 1000 == 909 or telefono // 100000 == 877):
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and telefono // 100000 != 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico y la hora de la llamada al usuario
telefono = int(input("Ingrese número telefónico (8 dígitos): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si se debe contestar la llamada o no
resultado = contestar_o_no(hora, telefono)

# Imprimir el resultado en la consola
print("Resultado:", resultado)

      