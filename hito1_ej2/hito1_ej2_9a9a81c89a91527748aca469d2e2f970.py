#Contestador de celular
telefono = (input("ingrese numero telefonico: "))
hora = int(input("ingrese hora: "))

p = int(telefono[5] + telefono[6] + telefono[7])
u = int(telefono[0] + telefono[1] + telefono[2])

if hora >= 0 and hora <=7:
    print("Contestar")
if hora > 7 and hora < 14:
    print("contestar")
elif hora >= 7 and hora < 14:
    print("No contestar")
if hora >= 17 and hora < 19 and u == 877:
    print("No contestar")
elif hora >= 17 and hora < 19:
    print("Contestar")
if hora > 19:
    print("No contestar")