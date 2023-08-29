#Contestador de celular
T = int(input("Ingrese telefono de 8 digitos: "))
while not (T>=10000000 and T<=99999999):
    T = input("Error. ingrese numero de 8 digitos: ")

H = int(input("Ingrese la hora (0-23): "))
while not(H>=0 and H<=23):
    H = int(input("Hora no valida. Ingrese la hora (0-23): "))

UT = T%1000
PT = T//100000

if (H>=0 and H <=7):
    print("CONTESTAR")
elif (H<14 and UT!=909):
    print("NO CONTESTAR")
elif (H<14 and UT==909):
    print("CONTESTAR")

elif (H>=14 and H<17):
    print("NO CONTESTAR")
elif (H>=17 and H<=19 and PT != 877):
    print("CONTESTAR")
elif (H>=17 and H<=19 and PT == 877):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")