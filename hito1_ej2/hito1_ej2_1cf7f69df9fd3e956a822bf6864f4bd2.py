telefono = int(input("Ingrese Celular de 8 Digitos: "))
while not(telefono>=10000000 and telefono<=99999999):
    telefono = int(input("Numero telefonico no válido [Debe ser de 8 digitos]: "))

hora = int(input("Ingrese la hora [0-23]: "))
while not(hora>=0 and hora<=23):
    hora = int(input("Hora no valida [0-23]: "))
ultimostres = telefono%1000
primerostres = telefono//100000

if (hora<=7):
    print("CONTESTAR")
else:
    if(hora<14):
        if(ultimostres == 909):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if(hora<=19):
            if(hora>=17 and hora<=19):
                if(primerostres == 877):
                    print("NO CONTESTAR")
                else:
                    print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        else:
            print("NO CONTESTAR")