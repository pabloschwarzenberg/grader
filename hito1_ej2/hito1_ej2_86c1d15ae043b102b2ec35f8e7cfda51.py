#Contestador de celular
numero_telefonico=int(input("Ingrese su numero telefonico de 8 cifras:"))
hora=int(input("Ingrese horario de su llamada:"))

if hora>0 and hora<7:
    print("CONTESTAR")

if hora>19:
    print("NO CONTESTAR")

if hora<14 and numero_telefonico%100000 == 909:
    print("Contestar")

if hora>17 and hora<19 or numero_telefonico//10000 == 877:
    print("No contestar")
else:
    print("Contestar")