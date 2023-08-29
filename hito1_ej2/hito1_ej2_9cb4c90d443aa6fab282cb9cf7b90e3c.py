#Contestador de celular
 
numTele = list(input("Ingrese número de teléfono: "))
if len(numTele)!=8:
    numTele = list(input("Ingrese número de telefono: "))
horaLlama = int(input("Ingrese hora de llamada: "))

if horaLlama < 0 or horaLlama > 23:
    horaLlama = int(input("Ingrese hora de llamada: "))
elif horaLlama >= 0 and horaLlama <= 7:
    print("CONTESTAR")
    
elif horaLlama <= 14 and horaLlama > 7: 
    if numTele[5] == "9" and numTele[6] == "0" and numTele[7] == "9":
        print("CONTESTAR")
        
elif horaLlama >= 17 and horaLlama <= 19 and numTele[0] != "8" and numTele[1] != "7" and numTele[2] != "7":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")  