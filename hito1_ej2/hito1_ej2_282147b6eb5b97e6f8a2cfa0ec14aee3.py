telefono=int(input("Ingrese el numero de telefono: "))
while not(telefono>=10000000 and telefono<=99999999):
    telefono=int(input("Error: el telefono debe ser de 8 digitos."))
hora=int(input("Ingrese la hora: "))
while not(hora>=0 and hora<=23):
    hora=int(input("Error: la hora debe ser en el rango 00 y 23."))
    
if(hora>=0 and hora<=7):
    print("CONTESTAR")
elif((hora<14) and (telefono%1000==909)):
    print("CONTESTAR")
elif((hora>=17)and(hora<=19)):
    print("NO CONTESTAR")
elif(telefono//100000==877):
    print("NO CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")