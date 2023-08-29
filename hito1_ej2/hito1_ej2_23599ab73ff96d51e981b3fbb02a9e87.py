#Contestador de celular
num_telefono=input("Introduzca el numero telefonico: ")
if len(num_telefono)==8:
    if num_telefono.isdigit():
        Contestar=num_telefono[5]+num_telefono[6]+num_telefono[7]
        no_contestar=num_telefono[0]+num_telefono[1]+num_telefono[2]
    else:
        print("error, permitido solo numeros")
else:
    print("error,debe ser de longitud 8, vuelva intentarlo")

hora=int(input("introduzca hora de llamada: "))
Num_hora=int(hora)
Num_contestar=int(Contestar)
Num_no_contestar=int(no_contestar)

if (hora>=0 and hora<=23):
    print("hora ok")
else:
    print("hora erronea, vuelva ingresar hora")

if (Num_hora>=0 and Num_hora<=7):
    print("CONTESTAR")
elif (Num_hora>=20 and Num_hora<=23):
    print("NO CONTESTAR")

elif (Num_hora>=8 and Num_hora<=13):
    if Num_contestar==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (Num_hora>=17 and Num_hora<=19):
    if Num_no_contestar==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
     