#Contestador de celular
Num=int(input("Ingrese su numero telefonico: "))
Hora=int(input("Ingrese hora de la llamada:  "))
if Hora >= 24 or Hora < 0:
    print("La hora debe ser entre 0 y 23 hrs")
elif Num <= 10000000 or Num >= 99999999:
    print("Tiene que ser un numero de 8 digitos")
else:
    ult=Num % 1000
    if Hora > 19:
        print("NO CONTESTAR")
    elif  Hora > 0 and Hora < 7:
        print("CONTESTAR")
    elif Hora > 7 and Hora < 14 and ult == 909:
       print("CONTESTAR")
    elif Hora > 17 and Hora < 19 and not ult == 877:
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")