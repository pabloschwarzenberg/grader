#Contestador de celular
NumeroTelefonico=int(input("Ingrese numero Telefonico: "))
while not(NumeroTelefonico>=10000000 and NumeroTelefonico<=99999999):
    NumeroTelefonico=int(input("por favor, Ingrese un Telefono valido de 8 numeros: "))
    
Hora= int(input("Ingrese la hora (0-23): "))
while not(Hora>=0 and Hora<=23):
    Hora=int(input("error, por favor ingrese una hora valida: "))

Ptresdigitos=NumeroTelefonico//100000
Utresdigitos=NumeroTelefonico%1000
                        
if (Hora>=0 and Hora<=7):
    print("CONTESTAR")
elif (Hora>7 and Hora<14):
    if Utresdigitos==909:
        print("CONTESTAR")
    else:
        print(" NO CONTESTAR")
elif (Hora>=17 and Hora<=19):
    if Ptresdigitos == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")   