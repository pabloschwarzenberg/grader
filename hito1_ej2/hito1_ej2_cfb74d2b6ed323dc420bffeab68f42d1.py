numero=input("Ingrese el número de teléfono: ")
hora=int(input("Ingrese la hora de la llamada entre las 0 y las 23: "))
digito=int(numero[-3]+numero[-2]+numero[-1])
digito2=int(numero[0]+numero[1]+numero[2])
if digito2==877:
    print("NO CONTESTAR")
elif digito==909  or (hora>=0 and hora<=7) or (hora>17 and hora<=19):
    print("CONTESTAR")
else:print("NO CONTESTAR")