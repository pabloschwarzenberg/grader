#Contestador de celular

numero = int(input("Ingrese un numero telefonico de 8 digitos: "))
hora = int(input("Ingrese la hora de llamada en formato 24 hrs: "))

extraer_subcadena1 = numero [1:5]
extraer_subcadena2 =numero [4:8]

if  (0 <= hora <= 7):
    print("CONTESTAR")

elif (7 < hora <= 14) and (extraer_subcadena1 == 909):
    print("CONTESTAR")

elif (14 < hora <= 16):
     print("NO CONTESTAR")

elif (17 <= hora <= 19) and (extraer_subcadena2 == 877) :
     print("CONTESTAR")

elif (hora > 19):
     print("NO CONTESTAR")

else:
     print("NO CONTESTAR")
      