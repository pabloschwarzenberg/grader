#Contestador de celular
telefono= int(input("Ingresa un numero telefonico de 8 digitos: "))
while not(telefono>=10000000 and telefono<=99999999):
    telefono= int(input("Error..El numero debe contener 8 digitos: "))
hora=int(input("Ingrese la hora [0-23]: "))
while not(hora>=0 and hora<=23):
    hora=int(input("Error...Ingrese la hora [0-23]: "))
ultimotres=telefono%1000
primerostres=telefono//100000

if(hora>=0 and hora<=7):
    print("CONTESTAR")
elif (hora<14 and ultimotres != 909):
    print("NO CONTESTAR")
elif(hora<14 and ultimotres==909):
    print("CONTESTAR")
elif(hora>=14 and hora<17):
    print("NO CONTESTAR")
elif(hora>=17 and hora<=19 and primerostres !=877):
    print("CONTESTAR")
elif(hora>=17 and hora<=19 and primerostres ==877):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")