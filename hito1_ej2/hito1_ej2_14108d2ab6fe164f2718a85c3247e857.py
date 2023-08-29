numero = int(input("Ingrese un numero telefonico de 8 cifras: "))
hora = int(input("Ingrese una hora (0 a 23): "))

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif numero % 1000 == 909:
    print("CONTESTAR")
elif hora>=17 and hora<=19 and numero // 100000 != 877:
    print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")