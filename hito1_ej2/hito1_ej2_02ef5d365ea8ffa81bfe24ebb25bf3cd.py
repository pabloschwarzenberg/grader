tel = input("Ingrese la hora: ")
hora = input("Ingrese el telefono: ")

if 0 <= int(hora) <= 7:
    print("CONTESTAR")

elif int(hora) <= 14:
    if int(tel[-3:]) == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

elif 17 <= int(hora) <= 19:
    if int(tel[0:3]) == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

else:
    print("NO CONTESTAR")




