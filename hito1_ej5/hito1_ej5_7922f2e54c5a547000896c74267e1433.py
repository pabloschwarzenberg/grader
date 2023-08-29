#Cálculo del dígito verificador de un rut
import math
import operator
rut = input("ingrese su rut sin digito verificador sin puntos ")
rut_list = []
num = [3,2,7,6,5,4,3,2]
num2 = [3,2,7,6,5,4,3]

for i in rut:
    rut_list.append(i)
    
rut_list_int = (int(x) for x in rut_list)


if rut.len()==8:
    calculo_verificador =list(map(operator.mul, rut_list_int, num))
elif rut.len()==7:
    calculo_verificador =list(map(operator.mul, rut_list_int, num2))



cal1 = sum(list(calculo_verificador))
cal2 = math.floor(cal1/11)
cal3 = cal1- (11*cal2)
cal4 = 11-cal3
dv = cal4

if cal4==11:
    dv = '0'
elif cal4==10:
    dv ='K'
    
print("dv =",dv,)
