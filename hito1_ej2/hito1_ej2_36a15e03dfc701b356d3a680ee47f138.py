number = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de llamada: "))
if hora >= 24 or hora <0:
    print("Hora debe ser entre 00 y 23 hrs")
elif number <=10000000 or number >= 99999999:
    print("Debe digitar un numero de 8 digitos")
else:
    ult=number %1000
    if hora >19:
        print("NO CONTESTAR")
    elif hora >0 and hora <7:
        print("CONTESTAR")
    elif hora >7 and hora <14 and ult ==909:
        print("CONTESTAR")
    elif hora >17 and hora <19 and not ult ==877:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")  