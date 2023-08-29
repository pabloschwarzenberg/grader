#Descomponer un número
numero = int (input ('ingrese numero de 3 digitos: '))
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
print ('Las centenas: ' + repr(centenas))
print ('Las decenas: ' + repr (decenas))
print ('Las unidades: ' + repr(unidades))