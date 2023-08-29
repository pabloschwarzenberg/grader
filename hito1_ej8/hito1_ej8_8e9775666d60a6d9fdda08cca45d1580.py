#Descomponer un número
import os

numero = int (input ('Ingresa el valor de numero: '))
miles=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
M1=(+ repr (miles))
C1=(+ repr (centenas))
D1=(+ repr (decenas))
U1=(+ repr (unidades))
print(M1"M"+C1"C"+D1"D"+U1"U")