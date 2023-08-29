#Cálculo del dígito verificador de un rut
import sys
import operator
import math


RUT = (input("Ingrese el RUT a validar (sin puntos): "))
print(RUT)
rutL = []  ##Lista, Separar rut ingresado numero a numero
num = [3,2,7,6,5,4,3,2] ##Lista, Numeros de Cálculo para obtener digito verificador, Modulo 11

for i in RUT: ##Recoore la lista
    rutL.append(i) ##agregar cualquier eleemnto

rutL_int = [int(x) for x in rutL]#recorre y Transfromar lista en numero entero

total = list(map(operator.mul, rutL_int, num))## Cálculo, multiplicación de La lista rutL_int por num para obtener el digito verificador.

calculo1 = sum(list(total))## Suma toda la lista
calculo2 = math.floor(calculo1 / 11) ##Divide por 11 y aproxima a numero menor en caso de decimales
calculo3 = calculo1 - (11 * calculo2)
calculo4 = 11 - calculo3 ##Obtenemos el resultado final 


verificador = calculo4 ##asignamos nueva variable 

if (calculo4 == 11):   ##Condiciones en caso de resultado igual 10 u 11
    verificador = "0"
elif(calculo4 == 10):
    verificador = "K"
    

print ("El digito verificador es: ", str(verificador), "\n"," el RUT es: ", str(RUT), "-", str(verificador))
      