#Contestador de celular
num = input("Ingrese número de teléfono: ")
hora = input("Ingrese hora de la llamada: ")

if int(hora) >= 0 and int(hora) <= 7:
    print("CONTESTAR")
elif int(hora) > 7 and int(hora) < 14:
    if num[5] == '9' and num[6] == '0' and num[7] == '9':
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif int(hora) >= 17 and int(hora) <= 19:
    if num[0] == '8' and num[1] == '7' and num[2] == '7':
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
elif int(hora) > 19:
    print("NO CONTESTAR")