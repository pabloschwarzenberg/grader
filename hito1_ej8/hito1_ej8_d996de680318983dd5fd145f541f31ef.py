#Descomponer un número

numero = int (input ('Ingresa el valor de numero: '))
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
print ('Valor de centenas: ' + repr (centenas))
print ('Valor de decenas: ' + repr (decenas))
print ('Valor de unidades: ' + repr (unidades))
print ()      