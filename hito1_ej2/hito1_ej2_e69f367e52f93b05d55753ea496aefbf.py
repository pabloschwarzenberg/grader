#Contestador de celular
numero_de_telefono = input("Ingrese el numero del telefono:")
hora_de_llamada = input("Ingrese la en que se ha llamado:")
x = int(numero_de_telefono)
y = int(hora_de_llamada)

if len(numero_de_telefono) == 8:
    if y > 00 and y < 7:
        print("CONTESTAR")
    else:
        if y > 7 and y < 14:
            if int(numero_de_telefono[5]) == 9:
                if int(numero_de_telefono[6]) == 0:
                    if int(numero_de_telefono[7]) == 9:
                        print("CONTESTAR")
    if y>14 and y<17:
        print("NO CONTESTAR")
    if y>17 and y<19:
        if int(numero_de_telefono[0])==8:
               if int(numero_de_telefono[1])==7:
                   if int(numero_de_telefono[2])==7:
                       print("NO CONTESTAR")
    if y>19 and y <=23:
        print("NO CONTESTAR")     