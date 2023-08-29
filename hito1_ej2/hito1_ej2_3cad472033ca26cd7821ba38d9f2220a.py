#Contestador de celular
Telefono = str(input("Ingrese un número a verificar: "))
Hora = int(input("Ingrese la Hora a consultar: "))
print("El numero ingresado es: {} ".format(Telefono))
TelefonoA = int(Telefono[0:3])
TelefonoB = int(Telefono[5:8])

if Hora >= 0 and Hora <= 7:
    print("Contesta puede ser urgente")

elif Hora < 14 and TelefonoB != 909:
    print("No contestar")

elif Hora < 14 and TelefonoB == 909:
    print("Contestar")
elif Hora >= 17 and Hora <= 19 and TelefonoA != 877:
    print("Contestar")
    

else:
    print("No contestar")
    

#############################################Validación de número#################################################
##Telefono = abs (int(Telefono))

##print("El numero ingresado es: {} ".format(Telefono))
##count = 0
##while Telefono > 0:
    ##Telefono //= 10
    ##count += 1
##if count <= 7:
    ##print("NUMERO NO SOPORTADO?? VERIFICAR NUMERO")
##elif count > 8:
    ##print("Numero No valido")
    
##elif count > 7 and count < 9:
    ##print("Telefono Valido!!! ")
##elif TelefonoA == 877:
    ##print("No contestar")
## print("Numbers of digits in your number is: {} ".format(count))
#################################################################################################################         