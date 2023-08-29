#Contestador de celular
fono = int(input("Ingrese número de telefono: "))
hora = int(input("Ingrese hora: "))

if fono>=0 and fono<=8:
    print("CONTESTAR")
if hora<14:
    if fono%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if hora>=17 and hora<=19:
    if fono//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if hora>19:
    print("NO CONTESTAR")
     