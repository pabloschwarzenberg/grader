#Descomponer un número
import os

numero = int (input ('Ingresa el valor de numero: '))
unmil=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
print (unmil,"M +" ,centenas, "C +" ,decenas, "D+" ,unidades, "U")
os.system ('pause')