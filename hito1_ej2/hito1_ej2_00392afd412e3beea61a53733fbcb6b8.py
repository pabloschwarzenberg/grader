numero = str(input("Ingrese el número que esta llamando: "))

hora = int(input("Ingrese la hora en la que se esta realizando la llamanda: "))

k = 5
j = 0

verificador1 = []
verificador2 = []

while k < 8:
    verificador1.append(numero[k])

    k = k+1

ext1 = int(verificador1[0])*100 + int(verificador1[1]) *10 + int(verificador1[2])    
while j < 4:
	verificador2.append(numero[j])

	j += 1

ext2 = int(verificador2[0])*100 + int(verificador2[1])*10 + int(verificador2[2])
if ((hora >= 7) and (hora <= 14)) and (909 == ext1):
    print ("CONTESTAR")

elif ((hora >= 7) and (hora <= 14)) and (909 != ext1):
            print ("NO CONTESTAR")

elif ((hora >=17) and (hora <= 19)) and (877 == ext2):
                print  ("NO CONTESTAR")

elif ((hora >=17) and (hora <= 19)) and (877 != ext2):
        print ("CONTESTAR")

elif ((hora > 19) and (hora <= 23)):
    print ("NO CONTESTAR")

else:
    if ((hora >=0) and (hora <=7)):
        print ("CONTESTAR")