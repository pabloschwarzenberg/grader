#Contestador de celular
numero = int(input("Ingrese el numero telefonico (de 8 cifras): "))
llamada = int(input("Ingrese la hora (sin minutos) de la llamada: "))

if llamada >= 00 and llamada <= 7:
    print("RESULTADO: CONTESTAR")
elif llamada <= 14 and str(numero).endswith("909"):
    print("RESULTADO: CONTESTAR")
elif llamada >= 17 and llamada <= 19 and str(numero).startswith("877"):
    print("RESULTADO: NO CONTESTAR")
else:
    print("RESULTADO: NO CONTESTAR")      