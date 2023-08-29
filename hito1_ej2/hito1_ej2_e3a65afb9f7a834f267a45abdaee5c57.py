#Contestador de celular
numero=int(input("ingrese numero de telefono:",))
hora=int(input("ingrese hora de llamada:",))
final= numero%1000
inicio= numero//100000
if(hora>0 and hora<=7):
    print("CONTESTAR")
if(hora<=14 and hora>7):
    if final == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(hora<=19 and hora>17):
    if inicio == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if(hora>19):
    print("NO CONTESTAR")   