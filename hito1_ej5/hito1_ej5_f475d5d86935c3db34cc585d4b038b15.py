#Cálculo del dígito verificador de un rut
#ENTRADA

rut = int(input("Ingrese rut sin digito verificador: "))

#PROCESAMIENTO
d1 = ((rut//1)%10) * 2
d2 = ((rut//10)%10) * 3
d3 = ((rut//100)%10) * 4
d4 = ((rut//1000)%10) * 5
d5 = ((rut//10000)%10) * 6
d6 = ((rut//100000)%10) * 7
d7 = ((rut//1000000)%10) * 2
d8 = (rut//10000000) * 3


suma = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8

division = suma // 11

multi = division * 11

resta = abs(multi - suma)

dv = 11 - resta

if dv == 11:
    print("dv = 0")
if dv == 10:
    print("dv = K")
else:
    print("dv =", dv)