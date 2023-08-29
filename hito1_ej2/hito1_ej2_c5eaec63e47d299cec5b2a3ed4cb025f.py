#ingresador de datos
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))

#operaciones y resultado

if hora >= 0 and hora < 7:
    print("Resultado: CONTESTAR")
elif hora < 14 and str(numero)[-3:] == "909":
    print("Resultado: CONTESTAR")
elif hora >= 17 and hora <= 19 and not str(numero).startswith("877"):
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
      