#Contestador de celular
Numero_Telefonico = input("ingrese el numero telefonico: ")
hora_llamada = int(input("ingrese la hora de la llamada: "))

while True:
    
    if len(Numero_Telefonico)>=7 and len(Numero_Telefonico)<=8:
        if (hora_llamada) >= 0 and hora_llamada <=7:
            print("CONTESTAR")

    if (hora_llamada) > 7 and hora_llamada < 14:
            no = int(Numero_Telefonico) % 1000
            if no == 909:
                print("CONTESTAR")
            else:
                if (hora_llamada) > 7 and hora_llamada < 14:
                    print("NO CONTESTAR")

    if (hora_llamada) > 16 and hora_llamada < 20:
            no = Numero_Telefonico [0:3]
            if no == str(877):
                print("NO CONTESTAR")
            else:
                if (hora_llamada) >= 17 and hora_llamada <=19:
                    print("CONTESTAR")
                    
    if (hora_llamada) > 19  and hora_llamada < 23:
        print("NO CONTESTAR")
    break    