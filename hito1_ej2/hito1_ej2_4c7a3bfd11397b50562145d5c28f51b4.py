#Contestador de celular
numero=int(input("Ingrese el telefono que quiere llamar: "))
hora_de_llamar=int(input("¿Hora de llamda?: "))
if(numero<=10000000 or numero>= 99999999):
   print("Tiene que ser un numero telefonico con 8 digitos")
elif(hora_de_llamar<0 and hora_de_llamar>=24):
    print("oh no, tiene que llamar entre o y 23 horas")
else:
    los_ultimos_digitos=numero%1000
    if(hora_de_llamar>0 and hora_de_llamar<7):
        print("CONTESTAR")
    elif (los_ultimos_digitos==909 and hora_de_llamar>7 and hora_de_llamar<14):
        print("CONTESTAR")
    elif (hora_de_llamar>19):
        print("NO CONTESTAR")
    elif (los_ultimos_digitos==877 and hora_de_llamar>17 and hora_de_llamar<19):
        print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
     