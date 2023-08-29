#Programa para descomponer un número
num = str (input("Por favor escribe un número de hasta cuatro dígitos: "))



if len(str(num)) > 4:
    print ("Solamente acepto números de 4 dígitos, no le pidas mucho a un código simple!")

elif len(str(num)) == 1:
    print (str(num) + "U")

elif len(str(num)) == 2:
    pos1 = int(num[0])
    pos2 = int(num[1])
    print (str(pos1) + "D" + " + " +  (str(pos2)) + "U")

elif len(str(num)) == 3:
    pos1 = int(num[0])
    pos2 = int(num[1])
    pos3 = int(num[2])
    print (str(pos1) + "C" +  " + " + str(pos2) + "D" + " + " + str(pos3) + "U")

elif len(str(num)) == 4:
    pos1 = int(num[0])
    pos2 = int(num[1])
    pos3 = int(num[2])
    pos4 = int(num[3])
    print (str(pos1) + "M" + " + " + str(pos2) + "C" + " + " + str(pos3) + "D" + " + " + str(pos4) + "U")
      