#Contestador de celular
#Ingreso número telefónico

Número = int(input("Ingrese el número telefónico: "))
while len(str(Número)) != 8:
    Número = int(input("Ingrese el número telefónico: "))

#Hora de la llamada
    
Hora = int(input("Ingrese la hora de la llamada: "))
while (Hora) < 0 or (Hora) > 23:
    Hora = int(input("Ingrese la hora de la llamada: "))

xNúmero = str(Número)

#Condición 1:

if (Hora) <= 7 and (Hora) >= 0:
    print("CONTESTAR, EMERGENCIA ⚠")
    
#Condición 2:

elif ((Hora) < 14 and (Hora) > 7) and (xNúmero[5] == "9" and xNúmero[6] == "0" and xNúmero[7] == "9"):
    print("Contestar")

elif ((Hora) < 14 and (Hora) > 7):
    print("NO CONTESTAR")

#Condición 3:

elif (xNúmero[0] != "8" and xNúmero[1] != "7" and xNúmero[2] != "7") and ((Hora) <= 19 and (Hora) >= 7):
    print("CONTESTAR")

elif (xNúmero[0] == "8" and xNúmero[1] == "7" and xNúmero[2] == "7") and ((Hora) <= 19 and (Hora) >= 7):
    print("NO CONTESTAR")
      
#Condición 4:
    
elif (Hora) > 19:
    print("NO CONTESTAR")