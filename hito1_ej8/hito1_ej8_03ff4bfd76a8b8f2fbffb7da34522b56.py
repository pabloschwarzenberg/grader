#Descomponer un número
numer =(input ('Ingresa numero de 4 digitos: '))
numero =int (numer)
largo = len(numer)
if largo > 4 :numer = input(("ingrese numero de cuatro digitos :"))
numero = int(numer)
largo =len(numer)
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
miles=((numero%10000-numero%1000)//1000)
unidades=numero%10
print (miles ,"M","+", centenas,"C","+" ,decenas,"D","+", unidades,"U")
if largo < 0 :print ("numero debe ser de 4 digitos")
