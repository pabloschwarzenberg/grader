#Contestador de celular
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
contestar = False

if 0 <= hora and hora <= 7:
    contestar = True
elif hora <= 14 and str(numero_telefonico).endswith("909"):
    contestar = True
elif 17 <= hora and hora <= 19 and not(str(numero_telefonico).startswith("877")):
    contestar = True

if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")