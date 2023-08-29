nro = int (input("ingrese numero de telefono de 8 digitos: "))
hora = int (input("ingrese hora de la llamada de 0 a 23: "))

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<=0 and hora>=7:
    print("NO CONTESTAR")
elif hora>2 and nro % 1000 == 909:
    print("CONTESTAR")
elif hora<2 and nro % 1000 != 909:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19 and nro // 100000 == 877:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")  