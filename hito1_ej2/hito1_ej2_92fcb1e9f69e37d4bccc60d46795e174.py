#Contestador de celular
NumCel = str(input("Ingrese numero de telefono: "))
Hora = int(input("Ingrese hora de llamado: "))

if (Hora > 0) and (Hora < 7):
    print("CONTESTAR")        
elif (Hora > 7 and Hora < 14) and (NumCel[5], NumCel[6], NumCel[7] == 909): 
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if (Hora > 17 and Hora < 19) and (NumCel[0], NumCel[1], NumCel[2] == 877):
    print("NO CONTESTAR")
else: 
    print("CONTESTAR")
if (Hora > 19):
    print("NO CONTESTAR")           