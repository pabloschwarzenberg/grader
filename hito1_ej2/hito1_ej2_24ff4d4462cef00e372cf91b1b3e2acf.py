nt=int(input("ingrese el numero telefonico:"))
while not (nt>=10000000 and nt<=99999999):
    nt= input("Error. ingrese un número que contenga 8 dígitos: ")
hvalida= int(input("Ingrese la hora dentro del rango 00:00 hasta las 23:00 hrs (es decir, 0-23): "))
while not(hvalida>=0 and hvalida<=23):
    hvalida= int(input("Hora invalida o fuera del margen pedido, por favor, ingrese una hora entre 0 y 23 horas: "))
er= nt%1000
fe= nt//100000

if (nt>=0 and hvalida <=7):
    print("CONTESTAR")
else:
    if (hvalida<14 and er==909):
        print("CONTESTAR")
    else:
        if (hvalida<14 and er!=909):
            print("NO Contestar")
        else:
            if (hvalida>=14 and hvalida<17):
                print("NO Contestar")
            else:
                if (hvalida>=17 and hvalida<=19 and fe != 877):
                    print("CONTESTAR")
                else:
                    if (hvalida>=17 and hvalida<=19 and fe == 877):
                        print("NO Contestar")
                    else:
                        print("NO Contestar")