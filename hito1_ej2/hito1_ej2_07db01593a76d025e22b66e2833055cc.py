numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

if 0 <= hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    print("CONTESTAR")
elif 17 <= hora_llamada <= 19 and numero_telefonico.startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
