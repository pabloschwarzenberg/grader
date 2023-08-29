num_telefonico = int(input("Ingrese su numero de telefono: "))
hora = int(input("Ingrese la hora: "))

if hora == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7:
    print("CONTESTAR")
while hora == 8 or 9 or 10 or 11 or 12 or 13 or 14:
    print(" NO CONTESTAR")
    if num_telefonico[5:8] == 909:
        print("CONTESTAR")