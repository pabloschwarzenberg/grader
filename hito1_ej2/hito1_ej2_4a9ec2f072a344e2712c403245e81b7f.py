#Contestador de celular
numero = int(input("Ingrese número de telefono de 8 digitos: "))
while not(numero >=10000000 and numero <=99999999):
    numero = int(input("ERROR, ¡Ingrese numero con 8 digitos!: "))

                 
hora = int(input("Ingrese la hora de 0 a 23 hrs: "))
while not (hora >=0 and hora <=23):
    hora = int(input("ERROR, ¡Ingrese la hora nuevamente de 0 hrs a 23 hrs!: "))

primeros_numeros = numero//100000
numeros_finales = numero%1000

if (hora >= 0 and hora <=7):
    print("CONTESTAR")
   
else:
    if(hora > 7 and hora <=14 and numeros_finales == 909):
     print("CONTESTAR")
    else:
         if (hora > 7 and hora <=14 and numeros_finales !=909):
             print ("NO CONTESTAR")   
    if (hora >= 17 and hora <= 19 and primeros_numeros == 877):
       print("NO CONTESTAR")
    else:
         if (hora >= 17 and hora <= 19 and primeros_numeros != 877):
            print("CONTESTAR")     
         if (hora >19 and hora <= 23):
            print("NO CONTESTAR")