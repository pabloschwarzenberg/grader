RutUsuario = input("ingrese su rut") #0
#Inicializacion de variables utilizadas en el programa
Factor = 2
Suma = 0
Modulo = 0
DigitoVer = 0
DvFinal = ""

#Recorre el rut ingresado caracter 
for i in RutUsuario[::-1]:

  Suma = Suma + int(i) * Factor
  Factor = Factor + 1
  if Factor > 7:
    Factor = 2
  
  print (int(i), " ", Suma)

Modulo=Suma%11
DigitoVer=11-Modulo

if DigitoVer == 11:
  DvFinal = 0
else:
  if DigitoVer == 10:
    DvFinal = "K"
  else:
    DvFinal = DigitoVer
    
print (" ")
print ("dv = ",DvFinal)