#Cálculo del dígito verificador de un rut
import sys    
import operator
import math

rut=input('Ingrese Rut :')
rut_list = []
num_cal = [3,2,7,6,5,4,3,2]
for i in rut:
  rut_list.append(i)
rut_list_int = [int(x) for x in rut_list]
calculo = list(map(operator.mul, rut_list_int, num_cal))
calculo1 = sum(list(calculo))
calculo2 = math.floor(calculo1 / 11)
calculo3 = calculo1 -(11 * calculo2)
calculo4 = 11 - calculo3
dv = calculo4
if (calculo4 == 11):
  dv = "0"
elif (calculo4 == 10):
  dv = "k"
print("Su DV ES: ",str(dv) + "\n", ("su rut completo :", str(rut)+"-" + str(dv)))