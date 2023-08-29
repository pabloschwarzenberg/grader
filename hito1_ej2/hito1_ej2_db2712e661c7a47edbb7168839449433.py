numero_telefonico = input("Ingrese Número terlefonico:")
hora_de_llamada = input("Ingrese hora de llamada:")
n = int(numero_telefonico)
h = int(hora_de_llamada)

if len(numero_telefonico) == 8:
    if h > 00 and h < 7:
        print("CONTESTAR")
    else:
        if h > 7 and h < 14:
            if int(numero_telefonico[5]) == 9:
                if int(numero_telefonico[6]) == 0:
                    if int(numero_telefonico[7]) == 9:
                        print("CONTESTAR")
    if h>14 and h<17:
        print("NO CONTESTAR")
    if h>17 and h<19:
        if int(numero_telefonico[0])==8:
               if int(numero_telefonico[1])==7:
                   if int(numero_telefonico[2])==7:
                       print("NO CONTESTAR")
    if h>19 and h <=23:
        print("NO CONTESTAR")
        
                