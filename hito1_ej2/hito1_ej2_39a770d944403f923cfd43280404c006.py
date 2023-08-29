hora = -1
telefono = 0
telefonoArray = [0]

while (len(telefonoArray) != 8):
    telefono = int(input(" ingrese el numero telefonico: "))
    telefonoArray = [int(d) for d in str(telefono)]
digitsIni = [telefonoArray[0], telefonoArray[1], telefonoArray[2]]
digitsFin = telefonoArray[-3:]

while (hora < 0 or hora > 23):    
    hora = int(input(" ingrese la hora de la llamada: "))

if (hora > -1 and hora < 8):
    print(" contestar ")
elif (hora > 7 and hora < 15 and digitsFin == [9,0,9]):
    print(" contestar ")
elif (hora > 16 and hora < 20 and digitsIni != [8,7,7]):
    print(" contestar ")
else:
    print(" no contestar ")