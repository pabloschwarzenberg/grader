#Contestador de celular
numero_telefonico=(input("ingresa el numero de telefono: "))
hora_llamada = int(input("ingrese la hora"))

x = numero_telefonico[0:8]
x_excluye = numero_telefonico[5:8]

if numero_telefonico == x:
    if(hora_llamada >= 0) and (hora_llamada <=7):
        print("CONTESTAR puede ser una emergencia")
    elif(x_excluye == str("909")) and (hora_llamada <= 14) and (hora_llamada >= 8):
        print("CONTESTAR")
    elif(hora_llamada == 17) and (hora == 19) and not (x_excluye) == str("877"):
        print("contesta la llamada mas tarde")
    else:
        print("NO CONTESTAR")
else:
    print("numero ingresado no valido")
      