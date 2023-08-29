#Contestador de celular
 telefono = int(input("ingrese telefono de 8 digitos: "))
while not (telefono>=10000000 and telefono<=99999999):
    telefono = int(input("error... ingrese telefono de 8 digitos: "))

hora = int(input("ingrese la hora (0-23): "))
while not (hora >= 0 and hora <= 23):
    hora = int(input("error... ingrese hora (0-23): "))

ultimostres = telefono%1000
primerostres = telefono//100000


#restriccion 1
if(hora>=0 and hora<=7):
    print("CONTESTAR")

#restriccion 2
elif(hora<14 and ultimostres != 909):
    print("NO CONTESTAR")
elif(hora<14 and ultimostres == 909):
    print("CONTESTAR")

#restriccion 3
elif(hora>=14 and hora<17):
    print("NO CONTESTAR")
elif(hora>=17 and hora<=19 and primerostres == 877):
    print("NO CONTETAR")
elif(hora>=17 and hora<=19 and primerostres != 877):
    print("CONTESTAR")

#restriccion 4
else:
    print("NO CONTESTAR")     