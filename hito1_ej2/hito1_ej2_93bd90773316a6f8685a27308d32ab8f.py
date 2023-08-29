#Contestador de celular
telefono = int(input("Ingrese numero telefonico : "))
hora = int(input("Ingrese hora de la llamada : "))
#Operacion
empiezaEn = telefono // 100000
terminaEn = telefono%1000
#print(terminaEn)
#Condicionales
if hora >= 0 and hora <= 7 :
    print("Contestar")
if hora <= 14 and terminaEn == 909 :
    print("Contestar")
elif hora <= 14 and terminaEn != 909 :
    print("No Contestar")
if hora >= 17 and hora <= 19 and empiezaEn == 877:
    print("No Contestar")
if hora >= 17 and hora <= 19 and empiezaEn != 877:
    print("Contestar")
if hora > 19 :
    print("No Contestar")
