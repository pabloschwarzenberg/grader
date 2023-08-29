hora=int(input("ingrese hora de llamada"))
numero=int(input("ingrese numero telefonico"))
if numero>0 and numero<7:
    print("CONTESTAR")
elif hora < 14 and str(numero)[-3:] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")



