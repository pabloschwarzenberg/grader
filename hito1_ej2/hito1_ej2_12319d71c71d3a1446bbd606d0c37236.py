#Contestador de celular
telefono = int(input("Ingrese un Numero Telefonico(8 digitos): "))
telefonostr = str(telefono)
num = telefonostr[5] + telefonostr[6] + telefonostr[7]
numi = telefonostr[0] + telefonostr[1] + telefonostr[2]
hora = int(input("Ingrese la hora de la llamada (0/23): "))

if hora <= 7 and hora >= 0:
    print("Ingresa un Numero Telefonico: ", telefono)
    print("Ingrese la hora de la llamada: ". hora)
    print("RESULTADO: CONTESTAR")
if hora < 14 and num == "909":
    print("Ingrese un Numero Telefonico: ", telefono)
    print("Ingrese la hora de la llamada: ", hora)
    print("RESULTADO: CONTESTAR")
if hora >= 17 and hora <= 19 and numi == "877":
    print("Ingrese un Numero Telefonico: ", telefono)
    print("Ingrese la hora de la llamada:", hora)
    print ("RESULTADO: NO CONTESTAR")
if hora > 19:
    print("Ingrese un Numero Telefonico: ", telefono)
    print("Ingrese la hora de la llamada: ", hora)
    print("RESULTADO: NO CONTESTAR ")