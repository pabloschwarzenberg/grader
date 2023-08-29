#Contestador de celular
N=int(input("ingrese su numero telefonico(8 digitos):"))
while not (N>=10000000 and N<=99999999):
    N=input("ERROR, ingrese su numero telefonico(8 digitos):")
h=int(input("ingrese la hora (0hrs a 23hrs):"))

ultimos_3_numeros=N%1000
primeros_3_digitos=N//100000
if (h>=0 and h<=7):
    print("contestar")
else:
    if(h<14 and ultimos_3_numeros!=909):
        print("no contestar")
    else:
        if (h<14 and ultimos_3_numeros==909):
            print("contestar")
        else:
            if (h>14 and h<17):
                print("no contestar")
            else:
                if (h>=17 and h<=19 and primeros_3_digitos!=877):
                    print("contestar")
                else:
                    if (h>=17 and h<=19 and primeros_3_digitos==877):
                        print("no contestar")
                    else:
                        print("no contestar")