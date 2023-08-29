t = int(input("Ingrese numero telefonico(8 digitos): "))
tstr = str(t)
num = tstr[5] + tstr[6] + tstr[7]
numi = tstr[0] + tstr[1] + tstr[2]
hora = int(input("Ingrese hora de la llamada (0/23): "))

if hora <= 7 and hora >= 0:
    print("Ingresa numero telefonico: ", t)
    print("Ingrese hora de la llamada: ". hora)
    print("RESULTADO: CONTESTAR")
if hora < 14 and num == "909":
    print("Ingrese numero telefonico: ", t)
    print("Ingrese hora de la llamada: ", hora)
    print("RESULTADO: CONTESTAR")
if hora >= 17 and hora <= 19 and numi == "877":
    print("Ingrese numero telefonico: ", t)
    print("Ingrese hora de la llamada:", hora)
    print ("RESULTADO: NO CONTESTAR")
if hora > 19:
    print("Ingrese numero telefonico: ", t)
    print("Ingrese hora de la llamada: ", hora)
    print("RESULTADO: NO CONTESTAR ")