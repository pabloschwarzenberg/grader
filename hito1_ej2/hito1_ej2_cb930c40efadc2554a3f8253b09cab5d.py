#Contestador de celular
NumeroTelefonico=input("Ingrese el numero de telefono que lo esta llamando: ")
if len(NumeroTelefonico)==8:
    number=[]
    for i in NumeroTelefonico:
        number.append(int(i))
    print(number)
    HoraLlamada=int(input("Ingrese la hora a la que se realizo la llamada: "))
    if HoraLlamada>=0 and HoraLlamada<=7:
        print("CONTESTAR!!!")
    elif HoraLlamada>7 and HoraLlamada<14 and number[5]==9 and number[6]==0 and number[7]==9:
        print("CONTESTAR!!!")
    elif HoraLlamada>7 and HoraLlamada<14:
        print("NO CONTESTAR!!!")
    elif HoraLlamada>=17 and HoraLlamada<=19 and number[0]==8 and number[1]==7 and number[2]==7:
        print("NO CONTESTAR!!!")
    elif HoraLlamada>=17 and HoraLlamada<=19:
        print("CONTESTAR!!!")
    elif HoraLlamada>19 and HoraLlamada<=23:
        print("NO CONTESTAR!!!")   
else:
    print("Ingrese un numero de telefono valido!!!")