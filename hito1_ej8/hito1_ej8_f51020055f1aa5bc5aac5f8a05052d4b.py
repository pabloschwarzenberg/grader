#Descomponer un número
numero = int(input("Ingrese numero de 4 digitos: "))
 
strNumero = str(numero)
largoNumero =len(strNumero)
if largoNumero>4:
  strNumero = strNumero[len(strNumero)-4:len(strNumero)]
  largoNumero = 4
  
strUnidad = "UDCM"
contador_unidad = 1
strDespliegue=""
strSigno=" + "

if largoNumero>4:
  largoNumero = 4

while largoNumero>0:

  strDespliegue =   strSigno + strNumero[largoNumero-1]+strUnidad[contador_unidad-1]  + strDespliegue
  if largoNumero==2:
      strSigno=""
  
  largoNumero -=1
  contador_unidad +=1
  
print(strDespliegue)