numero_telefono = eval(input("ingrese un numero de telefonode 8 digitos: "))
hora = eval(input("ingrese una hora: "))
comprobar_hora = (0<=hora<=23)

while True:
    siterminaen=str(numero_telefono)[5:8]
    siempiezaen=str(numero_telefono)[1:3]
    if comprobar_hora is True:
        if 0<=hora<=7:
            print("CONTESTAR")
            break
        elif 7<hora<=14 and siterminaen==909:
            print("NO CONTESTAR")
            break
        elif 7<hora<=14 and siterminaen == 909:
            print("CONTESTAR")
            break
        elif 17<hora<19 and siempiezaen==877:
            print("NO CONTESTAR")
            break
        elif 17<hora<19 and siempiezaen==877:
            print("CONTESTAR")
            break
        elif hora>=19:
            print("NO CONTESTAR")
            break
