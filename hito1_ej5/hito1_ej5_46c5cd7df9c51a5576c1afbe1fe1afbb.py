#Cálculo del dígito verificador de un rut
import operator
import math
rut = input("Ingrese los primeros 8 dígitos del RUT a verificar sin puntos ni guión: ")
rut_list = []
verificacion = [3,2,7,6,5,4,3,2]

for i in rut:
    rut_list.append(i)

rut_list_int = [int(x) for x in rut_list]
calculo = list(map(operator.mul, rut_list_int, verificacion))

calculo_total = sum(list(calculo))
calculo_total2 = math.floor(calculo_total // 11)
calculo_total3 = calculo_total - (11*calculo_total2)
calculo_final = 11 - calculo_total3

dv = calculo_final

if calculo_final == 11:
    dv = "0"
    
elif calculo_final == 10:
   dv = "K"

print(dv)