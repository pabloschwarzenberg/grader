#Cálculo del dígito verificador de un rut
import sys
import operator
import math


rut = (input("rut (primeros 7 digitos sin puntos): "))
rut_list = []
num_cal = [2,3,4,5,6,7]

for i in rut:
    rut_list.append(i)
    
rut_list_int = [int(x) for x in rut_list]   
    
calculo = list(map(operator.mul, rut_list_int, num_cal))   

calculo1 =sum(list(calculo))
calculo2 = math.floor(calculo1 / 11)
calculo3 = calculo1 - (11*calculo2)
calculo4 = 11 - calculo3

digito_verificador = calculo4

if(calculo == 11):
    digito_verificador = "0"
elif(calculo4 ==10):
    digito_verificador = "k"   
    
    
print("dv=" + str(digito_verificador))