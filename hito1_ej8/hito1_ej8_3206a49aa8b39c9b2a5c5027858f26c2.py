#Descomponer un número
n = 2345

if n<= 9999 :
  mil = n//1000
  centena = n//100 - mil*10 
  decena = n//10 - centena*10 - mil*100
  unidad = n - decena*10 - centena*100 - mil*1000

  #print(mil, centena, decena, unidad)

numero = int (input ('Ingresa el valor de numero: '))
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
milesima=(numero%100-numero%1000)//1000
decena_de_mil=(numero%1000-numero%10000)//10000
centena_de_mil=(numero%1000-numero%100000)//100000
unidades=numero%10
print ('Valor de centenas: ' + repr (centenas))
print ('Valor de decenas: ' + repr (decenas))
print ('Valor de milésima: ' + repr (milesima))
print ('Valor de decena_de_mil: ' + repr (decena_de_mil))
print ('centena_de_mil: ' + repr (centena_de_mil))
print ('cantidad de dígitos: ' + repr (unidades))