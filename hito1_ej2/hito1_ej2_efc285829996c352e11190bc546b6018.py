#Contestador de celular
num = int(input("Ingrese el numero telefonico: "))
while not(num>9999999 and num<100000000):
    num = int(input("Error, el numero debe ser de 8 digitos: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))
while not(hora>=0 and hora<=23):
    hora = int(input("Error, la hora ingresada no es valida"))
tresultimos=num%1000
tresprimeros=num//100000
if(hora<=7):
    print("Contestar")
elif(hora<14):
    if(tresultimos==909):
        print("Contestar")
    else:
        print("No contestar")
else:
    if(hora>=17 and hora<=19 and tresprimeros!=877):
        print("Contestar")
    else:
        print("No Contestar")
      