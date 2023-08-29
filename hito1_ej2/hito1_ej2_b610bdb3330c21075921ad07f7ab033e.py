
      # Entrada
telefono = str(input("Ingrese numero telefonico de 8 digitos:"))
hora = int(input("Ingrese hora:"))

# Prosceso
if hora > 0 and hora < 7:
    print("CONTESTAR")

if hora > 19 and hora <= 23:
    print("NO CONTESTAR")

# Mañana

else:
    if hora > 7 and hora < 14 and str(telefono [-3]) == "9" and str(telefono [-2]) == "0" and str(telefono [-1]) == "9":
        print("CONTESTAR")
   
    if hora > 7 and hora < 14 and str(telefono [-3]) != "9" and str(telefono [-2]) != "0" and str(telefono [-1]) != "9":
        print("NO CONTESTAR")
# Tarde
    if hora > 17 and hora < 19 and str(telefono [0:1]) == "8" and str(telefono [1:2]) == "7" and str(telefono [2:3]) == "7":
        print("NO CONTESTAR")
    
    if hora > 17 and hora < 19 and str(telefono [0:1]) != "8" and str(telefono [1:2]) != "7" and str(telefono [2:3]) != "7": 
        print("CONTESTAR")
