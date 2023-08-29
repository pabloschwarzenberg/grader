#Contestador de celular
Telefono = int(input("Ingrese el número de teléfonico:"))
if len(str(Telefono)) != 8:
    print("Número no valido, solo debe tener 8 digitos")
Hora = int(input("Ingrese horario:"))
Dia = 24

    
if Hora >= 0 and Hora <=7:
    print("CONTESTAR")

elif Hora < 14:
    excep = str(Telefono)[5:8]
    if excep == '909':
        print("CONTESTAR")
elif Hora >= 17 and Hora <= 19:
    excep = str(Telefono)[0:3]
    if excep == '877':
        print ("NO CONTESTAR")
elif Hora > 19:
    print("NO CONTESTAR")   