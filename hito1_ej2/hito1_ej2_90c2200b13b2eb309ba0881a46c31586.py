#Contestador de celular
while True:
    numero = input("Ingrese Numero de telefono :")
    if  len(numero) == 8 and numero.isdigit():
        break
    else:
        print("Ingrese un numero de 8 digitos")
while True:
    hora = input("Ingrese la hora en formato 0 - 23 :")
    if hora.isdigit():
        if int(hora) >= 0 and int(hora) <= 23:
            break
    else:
        print("Ingrese un dato correcto")
if int(hora) >= 0 and int(hora) <=7:
    print("CONTESTAR")
elif int(hora) >7 and int(hora) <14:
    verificacion = numero[5:]
    if verificacion == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif int(hora) >= 17 and int(hora) <= 19:
    verificacion = numero[:3]
    if verificacion == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")