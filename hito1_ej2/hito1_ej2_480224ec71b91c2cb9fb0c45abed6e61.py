#Contestador de celular
Numero=input("Ingrese el numero de celular (8 DIGITOS):")
Hora_llamada= float(input("Ingrese hora de llamada:"))
if 0>Hora_llamada <7:
    print("CONTESTAR")
if Hora_llamada <=14 and Numero[-3:]=="909":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if 17>Hora_llamada <19 and Numero[3:]=="877":
    print("CONTESTAR")
if Hora_llamada >=19:
    print("NO CONTESTAR")
     