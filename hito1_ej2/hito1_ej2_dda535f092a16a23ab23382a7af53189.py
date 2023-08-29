def contestar_o_no():
    numero = input("Ingrese numero telefonico: ")
    hora = int(input("Ingrese hora de la llamada: "))
    numero_str = str(numero)
    if numero_str.endswith('909') and hora < 14:
        print("Resultado: CONTESTAR")
    elif 0 <= hora < 7:  # Verificar si la hora es entre las 00:00 y las 07:00
        print("Resultado: CONTESTAR")
    elif 17 <= hora < 19 and not numero_str.startswith('877'):  # Verificar si la hora es entre las 17:00 y las 19:00 y el número no empieza con 877
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
contestar_o_no()      