#Contestador de celular
numero = 0
print ("Recuerde: el Numero de Telefono es de 8 digitos y la hora va de 0 a 24hrs")
while not (numero > 9999999 and numero < 100000000):
    numero = int(input("Ingrese Telefono: "))
hora = int(input("Ingrese Hora: "))
while (hora < 0 and hora > 23):
    hora = int(input("Ingrese Hora: "))

ultimos = numero%1000  
primeros = numero//100000     #12345678//1+cantidad de 0
print (primeros,",",ultimos)
if (hora <= 14 and ultimos == 909):
    print("CONTESTAR")
else:
    if (hora > 0 and hora < 7):
       print("CONTESTAR")
    elif (hora > 17 and hora < 19):
        if (primeros == 877):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    else:
        print("NO CONTESTAR")