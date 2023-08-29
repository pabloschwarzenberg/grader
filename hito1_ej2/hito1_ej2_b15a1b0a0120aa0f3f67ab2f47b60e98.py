#Contestador de celular
#ENTRADA

telefono = input("Ingrese numero telefonico: ")
hora = input("Ingrese hora de la llamada: ")
primeros = int(telefono[0:3])
ultimos = int(telefono[5:8])
hora= int(hora)

#DESARROLLO

if hora >= 0 and hora <= 7:
    print("CONTESTAR")

if hora > 7 and hora <= 13:
    if ultimos == 909:
        print("CONTESTAR")
    
    else:
        print("NO CONTESTAR")

if hora >= 14 and hora <= 16:
    print("NO CONTESTAR")
    
if hora >= 17 and hora <= 19:
    if primeros == 877:
        print("NO CONTESTAR")
    
    else:
        print("CONTESTAR")

if hora >= 20 and hora <= 23:
    print("NO CONTESTAR")