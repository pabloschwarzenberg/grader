#Contestador de celular
numero=str(input("Ingrese numero telefonico:"))
final=numero[5:]
inicio=numero[:3]
hora=int(input("Ingrese hora de la llamada:"))
if hora==0 and hora<7:
    print("CONTESTAR")
if hora<14 and final=="909":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if hora==17 and hora<19 and inicio=="877":
    print("NO CONTESTAR")
else:
    print("CONTESTAR")
if hora>19:
    print("NO CONTESTAR")      