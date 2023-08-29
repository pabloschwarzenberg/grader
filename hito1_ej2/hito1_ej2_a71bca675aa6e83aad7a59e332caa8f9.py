numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if 0 <= hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("CONTESTAR")
elif 17 <= hora_llamada < 19 and numero_telefonico // 1000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
