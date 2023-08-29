telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada (0-23) : "))

telefono = str(telefono)

primeros = telefono[0:3]
ultimos = telefono[5:]

if hora >= 0 and hora<=7:
    print("CONTESTAR")
elif hora < 14 and ultimos =='909':
    print("CONTESTAR")
elif hora>= 17 and hora<=19 and primeros != '877':
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")

