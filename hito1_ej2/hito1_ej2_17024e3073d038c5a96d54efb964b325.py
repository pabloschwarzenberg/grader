#Contestador de celular
numero = str(input("Ingrese el número que esta llamando: "))

hora = int(input("Ingrese la hora en la que se esta realizando la llamanda: "))

x = 5
h = 0

verificador1 = []
verificador2 = []

while x < 8:
    verificador1.append(numero[x])

    x = x+1

ext1 = int(verificador1[0])*100 + int(verificador1[1]) *10 + int(verificador1[2])    
while h < 4:
	verificador2.append(numero[h])

	h += 1

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