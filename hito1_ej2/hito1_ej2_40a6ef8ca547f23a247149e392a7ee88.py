#Contestador de celular
Numero= int(input("ingrese el numero de telefono de 8 digitos: "))
HoraLlamada= int(input("ingrese la hora de la llamada que se realiza entre las 0 y las 23: "))
UltimoNumero= Numero%1000
PrimerNumero= Numero//100000

if HoraLlamada<=0 and HoraLlamada<=7:
    print("Contestar por emergencia")

else:
    if HoraLlamada>7 and HoraLlamada<14 and UltimoNumero == 909:
        print("Contestar")
    else:
        if HoraLlamada>7 and HoraLlamada<14:
                print("No contestar")
        else:
                    if HoraLlamada>17 and HoraLlamada<19 and PrimerNumero == 877:
                        print("No contestar")
                    else:
                            if HoraLlamada>17 and HoraLlamada<19:
                                print("Contestar")
                            else:
                                if HoraLlamada>19:
                                    print("no contestar")
           


     