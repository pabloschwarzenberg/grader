#Descomponer un número
numero = int(input("Ingrese su numero:"))
numerostring = str(numero)
if len(str(numero)) == 1:
 print(numerostring[0] + "U")
elif len(str(numero)) == 2:
 print(numerostring[0] + "D + " + numerostring[1] + "U")
elif len(str(numero)) == 3:
 print(numerostring[0] + "C + " + numerostring[1] + "D + " + numerostring[2] + "U")
elif len(str(numero)) == 4:
 print(numerostring[0] + "M + " + numerostring[1] + "C + " + numerostring[2] + "D + " + numerostring[3] + "U")