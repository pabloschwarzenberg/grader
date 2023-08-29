#Contestador de celular
var_NumeroTelefono = int(input("Ingrese número telefónico: "))
while (len(str(var_NumeroTelefono)) != 8):
    var_NumeroTelefono = int(input("Ingrese número telefónico: "))
var_HoraLlamada = int(input("Ingrese hora de llamada: "))
while (var_HoraLlamada < 0 or var_HoraLlamada > 23):
    var_HoraLlamada = int(input("Ingrese hora de llamada: "))
if (var_HoraLlamada >= 0 and var_HoraLlamada <= 7):
    print("Resultado: CONTESTAR")
elif (var_HoraLlamada > 7 and var_HoraLlamada < 14):
    if (str(var_NumeroTelefono)[5:9] == "909"):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif (var_HoraLlamada >= 17 and var_HoraLlamada <= 19):
    if (str(var_NumeroTelefono)[0:3] == "877"):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
elif (var_HoraLlamada > 19):
    print("Resultado: NO CONTESTAR")