#Contestador de celular
telefono = str(input("Ingrese numero de telefono:"))
horario = int(input("Ingrese hora del llamado:"))
if horario > 0 and horario < 7:
    print("CONTESTAR")
elif horario > 19 and horario <= 23:
    print("NO CONTESTAR")
elif horario > 7 and horario < 14 and str(telefono[-3]) == "9" and str(telefono[-2]) == "0" and str(telefono[-1]) == "9":
    print("CONTESTAR")
elif horario > 7 and horario < 14 and str(telefono[-3]) != "9" and str(telefono[-2]) != "0" and str(telefono[-1]) != "9":
    print("NO CONTESTAR")
elif horario > 17 and horario < 19 and str(telefono[0]) == "8" and str(telefono[1]) == "7" and str(telefono[2]) == "7":
    print("NO CONTESTAR")
elif horario > 17 and horario < 19 and str(telefono[0]) != "8" and str(telefono[1]) != "7" and str(telefono[2]) != "7":
    print("CONTESTAR")
    