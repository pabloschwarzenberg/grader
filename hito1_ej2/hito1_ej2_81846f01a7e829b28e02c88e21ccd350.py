#Contestador de celular
 telefono = int(input("ingrese telefono de 8 digitos: "))
while not(telefono<=10000000 and telefono<=99999999):
    telefono = int(input("Erroooooor ingrese el numero de 8 digitos"))
hora = int(input("ingrese la hora [0-23]: "))
while not(hora>=0 and hora<=23):
    hora = int(input("Error"))
ultimostres = telefono%1000
primerostres = telefono//100000
if (hora>=0 and hora<=7):
    print("puedes CONTESTAR")
elif (hora<14 and ultimostres != 909):
    print("NO CONSTESTAR")
elif (hora>=14 and ultimotres == 909):
    print("puedes contestar")
elif (hora>=14 and hora<=17):
    print("no contestar")
elif (hora>=17 and hora<=19 and primerostres != 877):
    print("puedes contestar")
elif (hora>=17 and hora<=19 and primerostres == 877):
    print("no contestar")
else:
    print("NO CONSTESTAR")